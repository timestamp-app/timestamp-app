import logging
import json

import azure.functions as func

from uuid import uuid4
from datetime import datetime


def format_input(data):
    # Add azure info
    data["PartitionKey"] = str(datetime.today().year)
    data["RowKey"] = str(uuid4())

    # Change the datetime format from IFTTT to ISO
    ## For some reason azure tables will reformat the date on their end.
    ## This happens even if I pass it to them as a string.
    ifttt_time_fmt = "%B %d, %Y at %I:%M%p"
    data["time"] = datetime.strptime(data["time"], ifttt_time_fmt).isoformat()

    return data

def main(req: func.HttpRequest, storageOut: func.Out[str]) -> func.HttpResponse:
    logging.info('Function processed a request.')

    # Get Input
    try:
        req_body = req.get_json()
    except:
        logging.info('Request Failed: No JSON input supplied.')
        return func.HttpResponse("Requires JSON input", status_code=400)

    # Format input
    try:
        req_body = format_input(req_body)
    except:
        logging.info('Request Failed: Could not format input.')
        return func.HttpResponse("Could not format input", status_code=500)

    # Write input
    try:
        storageOut.set(json.dumps(req_body))
    except:
        logging.error('Request Failed: Could not write to storage.')
        return func.HttpResponse("Could not write to storage", status_code=500)

    return func.HttpResponse("Success")
