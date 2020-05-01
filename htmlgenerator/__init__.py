import os
import logging
import json

import azure.functions as func
from azure.storage.blob import BlobServiceClient, ContentSettings

from . import generator


def main(req: func.HttpRequest, recordsJSON, context: func.Context):
    logging.info('HTML Generator function processed a request.')

    try:
        records = json.loads(recordsJSON)
    except:
        logging.error('Error reading records.')
        return func.HttpResponse("Error reading records", status_code=500)

    try:
        working_directory = context.function_directory

        gen = generator.generator(records)
        gen.make_plots()
        html = gen.make_html(working_directory)
    except:
        logging.error('Error making html.')
        return func.HttpResponse("Error making html", status_code=500)

    try:
        content_settings = ContentSettings(content_type="text/html")

        connection_string = os.environ["AzureWebJobsStorage"]
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container="$web", blob="index.html")
        blob_client.upload_blob(html, overwrite=True, content_settings=content_settings)
    except:
        logging.error('Error writing html.')
        return func.HttpResponse("Error writing html", status_code=500)

    return func.HttpResponse("Success")
