# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import os
from typing import List
from azure.storage.blob import BlobServiceClient


def main(name: str) -> List[str]:
    logging.log(logging.INFO, f"getInputDataFn -> {name}")
    blob_service_client = BlobServiceClient.from_connection_string(
        "DefaultEndpointsProtocol=https;AccountName=mapreduce2;AccountKey=oE8QF/tQ41ZG8OE8BIBD+3UNt9OfNSyt4WPxXJYAXQoGmsexnmRCYuYLMdi5Ezw0CrIROZ5b4PzM+AStytU4lg==;EndpointSuffix=core.windows.net")
    container_client = blob_service_client.get_container_client("mrinput")

    # for blob in container_client.list_blobs():
    #     logging.log(logging.INFO, f"getInputDataFn -> {blob.name}")

    # return "ok"
    # return list(container_client.list_blobs())
    return [
        container_client.download_blob(blob.name).readall().decode("utf-8")
        for blob in container_client.list_blobs()
    ]
