import os
import logging
import json

import azure.functions as func
from azure.storage.blob import BlobServiceClient

from . import generator


def main(req: func.HttpRequest, recordsJSON):
    logging.info('HTML Generator function processed a request.')

    try:
        records = json.loads(recordsJSON)
    except:
        logging.error('Error reading records.')

    gen = generator.generator(records)
    gen.make_plots()
    html = gen.make_html()

    connection_string = os.environ["AzureWebJobsStorage"]
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container="$web", blob="index.txt")
    blob_client.upload_blob(html, overwrite=True)

    return func.HttpResponse("Success")
