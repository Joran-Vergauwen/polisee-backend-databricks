from azure.storage.blob import BlobServiceClient
import os
import logging
import tempfile
import tiktoken
import re
import json

from pathlib import Path

import datetime

from langchain_community.document_loaders import PyMuPDFLoader
from azure.cosmos import CosmosClient
from openai_functions.config import (METADATA)

def get_all_dates_to_score(start_date, end_date, cosmos_db_account_uri, cosmos_db_account_key, cosmos_db_database_name, cosmos_db_container_name):
    date_statuses = []
    downloaded_doc = []
    if start_date is None:
        client = CosmosClient(cosmos_db_account_uri, credential=cosmos_db_account_key)
        database = client.get_database_client(cosmos_db_database_name)
        container = database.get_container_client(cosmos_db_container_name)

        dates_to_score = []
        new_files = []
        today = datetime.datetime.today().strftime('%Y%m%d')
        
        # Get dates with new files
        for item in container.query_items(
            # query='SELECT * FROM poliseecontainer where poliseecontainer.statusScraping = "success" and (not IS_DEFINED(poliseecontainer.statusScoring) or (poliseecontainer.statusScoring != "success" and poliseecontainer.statusScoring != "skip"))',
            query = f'SELECT * FROM poliseecontainer where poliseecontainer.statusScoring = "waiting"',
            enable_cross_partition_query=True):
            try:
                downloaded_doc += item["downloadedDoc"]
                dates_to_score += [x[21:31] for x in downloaded_doc]
                
                # dates_to_score += [item["scrapedDate"][0:4] + "/" + item["scrapedDate"][4:6] + "/" + item["scrapedDate"][6:8]]
                # date_statuses += [item]  
            except:
                # print("no new docs")
                pass
        
        dates_to_score = list(set(dates_to_score))
        dates_to_score_cleaned = [x.replace("/", "") for x in dates_to_score]
    else: 
        # Get dates between start date and end date
        start_date_d = datetime.datetime.strptime(start_date, "%Y/%m/%d").date()
        end_date_d = datetime.datetime.strptime(end_date, "%Y/%m/%d").date()
        dates_to_score = []
        for i in range((end_date_d - start_date_d).days +1):
            dates_to_score += [str(start_date_d + datetime.timedelta(days=i)).replace("-", "/")]
        dates_to_score_cleaned = [x.replace("/", "") for x in dates_to_score]

    # Get for all of these dates the status
    dates_to_score_str = '(' + ', '.join(f"'{item}'" for item in dates_to_score_cleaned) + ')'
    for item in container.query_items(
        # query='SELECT * FROM poliseecontainer where poliseecontainer.statusScraping = "success" and (not IS_DEFINED(poliseecontainer.statusScoring) or (poliseecontainer.statusScoring != "success" and poliseecontainer.statusScoring != "skip"))',
        query = f'SELECT * FROM poliseecontainer where poliseecontainer.scrapedDate in {dates_to_score_str}',
        enable_cross_partition_query=True):
            try:
                date_statuses += [item]  
            except:
                # print("no new docs")
                pass

    return dates_to_score, date_statuses, dates_to_score_str

def copy_pdf_from_blob_locally(storage_account_name, storage_account_key, container_name, cloud_metadata):
    temp_dir = tempfile.gettempdir()
    blob_name = cloud_metadata["cloud_path"]
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    logging.info(blob_client)

    # Download blob content to local path
    local_pdf_path = os.path.join(temp_dir, cloud_metadata["filename"])
    with open(local_pdf_path, "wb") as local_file:
        blob_data = blob_client.download_blob()
        local_file.write(blob_data.readall())
    
    return local_pdf_path

def copy_pdf_from_blob_locally_output(storage_account_name, storage_account_key, container_name, container, filename):

    """
    Downloads a PDF file from a blob in Azure Storage to a local path.

    Parameters:
    - storage_account_name (str): The name of the Azure Storage account.
    - storage_account_key (str): The access key for the Azure Storage account.
    - container_name (str): The name of the container where the blob is stored.
    - blob_name (str): The name of the blob containing PDF content.
    - local_path (str): The local path where the PDF file will be saved.

    Returns:
    str: The local path of the downloaded PDF file.

    The function connects to the specified Azure Storage account and container, downloads the content of the specified blob,
    and saves the PDF file to the specified local path.

    Example:
    local_pdf_path = download_pdf_from_blob(
        storage_account_name="your_storage_account_name",
        storage_account_key="your_storage_account_key",
        container_name="your_container_name",
        blob_name="your_blob_name.pdf",
        local_path="local_directory"
    )
    print(local_pdf_path)
    """
    temp_dir = tempfile.gettempdir()
    blob_name = container + "/" + filename
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    logging.info(blob_client)

    # Download blob content to local path
    local_pdf_path = os.path.join(temp_dir, filename)
    with open(local_pdf_path, "wb") as local_file:
        blob_data = blob_client.download_blob()
        local_file.write(blob_data.readall())

    return local_pdf_path

def read_pdf_page_by_page(path):
    logging.info(f"path: {path}")
    loader = PyMuPDFLoader(path)
    data = loader.load()
    pages = []

    for page_number, document in enumerate(data):
        # Clean the page content
        document.page_content=re.sub('\n', '', document.page_content)

        encoding = tiktoken.get_encoding("cl100k_base")
        encoded_content = encoding.encode(document.page_content)
        num_tokens = len(encoding.encode(document.page_content))

        if num_tokens > 8000:
            # Splitting the page content into two halves
            half_length = len(encoded_content) // 2
            first_half = encoded_content[:half_length]
            second_half = encoded_content[half_length:]

            # Decode the halves back to text
            first_half_text = encoding.decode(first_half)
            second_half_text = encoding.decode(second_half)

            # Add the halves as separate pages
            pages.append(first_half_text)
            pages.append(second_half_text)
        else:
            # If token count is not greater than 8000, add the whole content as one page
            pages.append(encoding.decode(encoded_content))          
    logging.info(f'pages  {pages}')
    return pages

## DEPRECATED
def download_pdf_from_blob(storage_account_name, storage_account_key, container_name, container, filename, local_path):

    """
    Downloads a PDF file from a blob in Azure Storage to a local path.

    Parameters:
    - storage_account_name (str): The name of the Azure Storage account.
    - storage_account_key (str): The access key for the Azure Storage account.
    - container_name (str): The name of the container where the blob is stored.
    - blob_name (str): The name of the blob containing PDF content.
    - local_path (str): The local path where the PDF file will be saved.

    Returns:
    str: The local path of the downloaded PDF file.

    The function connects to the specified Azure Storage account and container, downloads the content of the specified blob,
    and saves the PDF file to the specified local path.

    Example:
    local_pdf_path = download_pdf_from_blob(
        storage_account_name="your_storage_account_name",
        storage_account_key="your_storage_account_key",
        container_name="your_container_name",
        blob_name="your_blob_name.pdf",
        local_path="local_directory"
    )
    print(local_pdf_path)
    """
    blob_name = container + "/" + filename
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    logging.info(blob_client)

    # Download blob content to local path
    local_pdf_path = os.path.join(local_path, filename)
    with open(local_pdf_path, "wb") as local_file:
        blob_data = blob_client.download_blob()
        local_file.write(blob_data.readall())

    return local_pdf_path

def get_all_filepaths(storage_account_name, storage_account_key, container_name, root_folders, dates_to_score):
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"

    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    cloud_paths = {}
    for date_to_score in dates_to_score: # Loop over all dates
        # date_to_score = date_status["scrapedDate"][0:4] + "/" + date_status["scrapedDate"][4:6] + "/" + date_status["scrapedDate"][6:8]
        cloud_paths[date_to_score] = []
        blob_list = container_client.list_blobs(name_starts_with=root_folders + date_to_score) # TODO add filters
        for blob in blob_list: # Get all AI output files
            new_metadata = {}
            new_metadata["filename"] = blob["name"][blob["name"].rfind("/") + 1 :]
            new_metadata["cloud_path"] = blob["name"]
            new_metadata["root_folders"] = root_folders
            policy_level_tmp = blob["name"].replace(root_folders, "")[11:]
            new_metadata["policy_level_fr"] = METADATA["policy_levels"][policy_level_tmp[:policy_level_tmp.find("/")]]["fr"]
            new_metadata["policy_level_nl"] = METADATA["policy_levels"][policy_level_tmp[:policy_level_tmp.find("/")]]["nl"]
            new_metadata["local_path"] = ""
            cloud_paths[date_to_score] += [new_metadata]
        if cloud_paths[date_to_score] == []:
            cloud_paths.pop(date_to_score)


    return cloud_paths

def load_all_output_jsons(storage_account_name, storage_account_key, container_name, start_date, end_date):
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"

    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    # Get dates between start date and end date
    start_date_d = datetime.datetime.strptime(start_date, "%Y/%m/%d").date()
    end_date_d = datetime.datetime.strptime(end_date, "%Y/%m/%d").date()
    dates_scored = []
    for i in range((end_date_d - start_date_d).days +1):
        dates_scored += [str(start_date_d + datetime.timedelta(days=i)).replace("-", "/")]

    # Get all relevant files
    data = []
    names = []
    for date_between in dates_scored: # Loop over all dates
        blob_list = container_client.list_blobs(name_starts_with="ai_output/" + date_between) # TODO add filters
        for blob in blob_list: # Get all AI output files
            names += [blob["name"]]
            new_path = copy_pdf_from_blob_locally_output(
                storage_account_name,
                storage_account_key,
                "polisee",
                blob['name'][0:blob['name'].rfind('/')],
                blob['name'][blob['name'].rfind('/')+1:]
            )
            new_data = json.loads(Path(new_path).read_text())
            if data == []:
                data = new_data
            else:
                data += new_data
    
    return data, names, start_date_d, end_date_d, dates_scored

def filter_topics(data, topics):
    topics = [x.lower() for x in topics]
    output = [d for d in data if d['topic'].lower() in topics] if (topics != [""]) else data
    return output


    

    
