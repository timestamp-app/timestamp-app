import os
import requests
import logging
import json

import azure.functions as func

from uuid import uuid4
from datetime import datetime


def format_input(data):
    # Add azure info
    data["PartitionKey"] = str(datetime.today().year)
    data["RowKey"] = str(uuid4())

    # Change the datetime format from IFTTT
    # Was going to use ISO but azure tables detects that format and changes it
    ifttt_time_fmt = "%B %d, %Y at %I:%M%p"
    prefered_time_fmt = "%Y/%m/%d %H:%M"
    datetime_obj = datetime.strptime(data["time"], ifttt_time_fmt)
    data["time"] = datetime_obj.strftime(prefered_time_fmt)

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

    # Trigger HTML Generator
    try:
        gen_url = 'https://' + os.getenv("WEBSITE_HOSTNAME") + '/api/htmlgenerator'
        payload = {'code': os.getenv("HTMLGENERATOR_KEY")}
        r = requests.get(gen_url, params=payload)
    except requests.exceptions.HTTPError as e:
        logging.error("Invalid response code form html generator: " + e.response)
        return func.HttpResponse("Invalid response code form html generator: " + e.response, status_code=500)
    except:
        logging.error("Couldnt trigger html generator")
        return func.HttpResponse("Couldnt trigger html generator", status_code=500)

    return func.HttpResponse("Success")
