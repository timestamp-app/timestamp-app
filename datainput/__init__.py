import logging
import json

import azure.functions as func

from uuid import uuid4
from datetime import datetime


def main(req: func.HttpRequest, storageOut: func.Out[str]) -> func.HttpResponse:
    logging.info('Function processed a request.')

    # Get Input
    try:
        req_body = req.get_json()
    except:
        logging.info('Request Failed: No JSON input supplied.')
        return func.HttpResponse("Requires JSON input", status_code=400)

    # Write input
    try:
        req_body["PartitionKey"] = str(datetime.today().year)
        req_body["RowKey"] = str(uuid4())
        # Change the datetime format from IFTTT to ISO 
        req_body["time"] = datetime.strptime(req_body["time"], "%B %d, %Y at %I:%M%p").isoformat()

        storageOut.set(json.dumps(req_body))
    except:
        logging.error('Request Failed: Could not write to storage.')
        return func.HttpResponse("Could not write to storage", status_code=500)

    return func.HttpResponse("Success")
