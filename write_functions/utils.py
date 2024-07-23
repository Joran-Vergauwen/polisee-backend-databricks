import json
import logging
from azure.storage.blob import BlobServiceClient

from azure.cosmos import CosmosClient

def write_json_to_blob(data, storage_account_name, storage_account_key, container_name, cloud_metadata):
    blob_name = cloud_metadata["cloud_path"].replace("scraped_data/files", "ai_output").replace(".pdf", ".json")
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    logging.info(blob_client)

    # Convert JSON data to a string
    json_string = json.dumps(data)

    # Upload the JSON string to the blob
    blob_client.upload_blob(json_string, overwrite=True)
    return blob_name


def update_status_cosmos_db(succeeded, status, cosmos_db_account_uri, cosmos_db_account_key, database_name, container_name):
    status["statusScoring"] = "success" if succeeded else "failed"

    client = CosmosClient(cosmos_db_account_uri, credential=cosmos_db_account_key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
    container.upsert_item(status)
    