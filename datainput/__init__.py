"""
This module is responsible for ingesting data and writing it to storage
"""
import logging
from datetime import datetime

import azure.functions as func

from .data_wrangler import DataWrangler
from ..helpers.error_handling import handle_error
from ..helpers.notifications import push_notification


# pylint: disable=E1136,W0702
def main(req: func.HttpRequest, storageout: func.Out[str]) -> func.HttpResponse:
    """
    This function takes in a http request, formats the data, and writes it to storage
    :param req:
    :param storageout:
    :return:
    """
    logging.info('Function processed a request.')

    if req.url == '/api/datainput/healthcheck':
        return func.HttpResponse("Healthy")

    # Get Input
    try:
        req_body = req.get_json()
        wrangler = DataWrangler(req_body)
    except:
        logging.info('Request Failed: No JSON input supplied.')
        return func.HttpResponse("Requires JSON input", status_code=400)

    # Format input
    try:
        wrangler.add_key_values()
        wrangler.format_time()
    except:
        return handle_error('Request Failed: Could not format input.')

    # Write input
    try:
        wrangler.write_to_table(table=storageout)
    except:
        return handle_error('Request Failed: Could not write to storage.')

    push_notification("Success", "Record added at: " + str(datetime.now()))
    return func.HttpResponse("Success")
