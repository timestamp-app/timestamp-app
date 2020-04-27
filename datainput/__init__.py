import logging
import json
import uuid
import datetime

import azure.functions as func


def main(req: func.HttpRequest, storageOut: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Get Input
    try:
        req_body = req.get_json()
    except:
        logging.info('Request Failed: No JSON input supplied.')
        return func.HttpResponse("Requires JSON input", status_code=400)

    # Write input
    try:
        req_body["PartitionKey"] = str(datetime.date.today().year)
        req_body["RowKey"] = str(uuid.uuid4())

        storageOut.set(json.dumps(req_body))
    except:
        logging.error('Request Failed: Could not write to storage.')
        return func.HttpResponse("Could not write to storage", status_code=500)

    return func.HttpResponse("Success")
