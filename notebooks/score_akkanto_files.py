# Databricks notebook source
dbutils.widgets.text("start_date", "")
dbutils.widgets.text("end_date", "")
dbutils.widgets.text("root_folders", "polisee")

# COMMAND ----------

import langchain_core
print(langchain_core.__version__)

# COMMAND ----------

from config.config import STORAGE_ACCOUNT_NAME, STORAGE_ACCOUNT_KEY, COSMOS_DB_ACCOUNT_URI, COSMOS_DB_ACCOUNT_KEY, COSMOS_DB_DATABASE_NAME, COSMOS_DB_CONTAINER_NAME, APPINSIGHTS_INSTRUMENTATIONKEY
from read_functions.utils import (copy_pdf_from_blob_locally, 
                                  read_pdf_page_by_page, 
                                  load_all_output_jsons, 
                                  filter_topics, 
                                  get_all_filepaths,
                                  get_all_dates_to_score)
from write_functions.utils import (write_json_to_blob, update_status_cosmos_db)

from openai_functions.utils import generate_output_type_by_type
import logging # Configure logging logging.basicConfig(level=logging.INFO, # Set the logging level to INFOformat='%(asctime)s - %(levelname)s - %(message)s') # Log an info messagelogging.info("This is an informational message.")

import datetime

# COMMAND ----------

start_date = dbutils.widgets.get("start_date") if dbutils.widgets.get("start_date") != "" else None
end_date = dbutils.widgets.get("end_date") if dbutils.widgets.get("end_date") != "" else None
root_folders = dbutils.widgets.get("root_folders")

# COMMAND ----------

dates_to_score, date_statuses, dates_to_score_str = get_all_dates_to_score(start_date, end_date, COSMOS_DB_ACCOUNT_URI, COSMOS_DB_ACCOUNT_KEY, COSMOS_DB_DATABASE_NAME, COSMOS_DB_CONTAINER_NAME)

cloud_metadata_s  = get_all_filepaths(STORAGE_ACCOUNT_NAME, STORAGE_ACCOUNT_KEY, "polisee", root_folders, dates_to_score)

try:
    AI_output, result_tmp = [], []
    for date_status in date_statuses:
        date_to_score = date_status["scrapedDate"][0:4] + "/" + date_status["scrapedDate"][4:6] + "/" + date_status["scrapedDate"][6:8]
        if date_to_score in cloud_metadata_s: # Check if there were files for this date
            failed_run = False

            # Loop over all documents
            for i in range(len(cloud_metadata_s[date_to_score])):
                cloud_metadata = cloud_metadata_s[date_to_score][i]

                # Copy pdf locally
                try:
                    local_pdf_path = copy_pdf_from_blob_locally(STORAGE_ACCOUNT_NAME, STORAGE_ACCOUNT_KEY, "polisee", cloud_metadata)
                    cloud_metadata["local_path"] = local_pdf_path
                    cloud_metadata_s[date_to_score][i] = cloud_metadata
                except Exception as e:
                    failed_run = True
                    print(f"Error in copy_pdf_from_blob_locally: {e}")
                # Get pages
                try:
                    pages = read_pdf_page_by_page(local_pdf_path)
                except Exception as e:
                    failed_run = True
                    print(f"Error in read_pdf_page_by_page: {e}")

                # Generate output page by page
                try:
                    new_output, result_tmp = generate_output_type_by_type(pages, date_to_score, cloud_metadata)
                    AI_output += [new_output]
                except Exception as e:
                    failed_run = True
                    print(f"Error in generate_output_type_by_type: {e}")

                # Write output to blob storage
                try:
                    output_path = write_json_to_blob(new_output, STORAGE_ACCOUNT_NAME, STORAGE_ACCOUNT_KEY, "polisee", cloud_metadata)
                    cloud_metadata["output_path"] = output_path
                    cloud_metadata_s[date_to_score][i] = cloud_metadata
                except Exception as e:
                    failed_run = True
                    print(f"Error in write_json_to_blob: {e}")
            # Update cosmos db        
            if failed_run:
                update_status_cosmos_db(False, date_status, COSMOS_DB_ACCOUNT_URI, COSMOS_DB_ACCOUNT_KEY, COSMOS_DB_DATABASE_NAME, COSMOS_DB_CONTAINER_NAME)
            else: 
                update_status_cosmos_db(True, date_status, COSMOS_DB_ACCOUNT_URI, COSMOS_DB_ACCOUNT_KEY, COSMOS_DB_DATABASE_NAME, COSMOS_DB_CONTAINER_NAME)
except Exception as e:
    # Update cosmos DB
    failed_run = True
    print(f"Error in for loop: {e}")

# COMMAND ----------

cloud_metadata_s
