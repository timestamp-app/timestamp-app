"""
This module is responsible for generating a static website from the data in the table
"""

import json
import logging
import os

import azure.functions as func
from azure.storage.blob import BlobServiceClient, ContentSettings

from . import generator


# pylint: disable=W0702
def main(recordsjson, context: func.Context):
    """
    This function reads the data from the table and converts it into a html page
    :param recordsjson: The json input from the azure table
    :param context: The context in which the function is run (used to get working directory)
    :return:
    """
    logging.info('HTML Generator function processed a request.')

    try:
        records = json.loads(recordsjson)
    except:
        logging.error('Error reading records.')

    try:
        working_directory = context.function_directory

        gen = generator.Generator(records)
        gen.make_plots()
        html = gen.make_html(working_directory)
    except:
        logging.error('Error making html.')

    try:
        content_settings = ContentSettings(content_type="text/html")

        connection_string = os.environ["AzureWebJobsStorage"]
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container="$web", blob="index.html")
        blob_client.upload_blob(html, overwrite=True, content_settings=content_settings)
    except:
        logging.error('Error writing html.')
