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


def push_notification(code, message):
    try:
        wirepusher_url = 'https://wirepusher.com/send'
        payload = {
            'id': os.getenv("WIREPUSHER_ID"),
            'title': 'Timestamp ' + code,
            'message': message,
            'type': code
            } 
        requests.get(wirepusher_url, params=payload)
    except requests.exceptions.HTTPError as e:
        logging.error("Request Failed: Invalid response code from wirepusher: " + e.response)
    except:
        logging.error("Request Failed: Couldnt trigger wirepusher")


def handle_error(message, code=500):
    logging.error(message)
    push_notification("Error", message)
    return func.HttpResponse(message, status_code=code)


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
        return handle_error('Request Failed: Could not format input.')

    # Write input
    try:
        storageOut.set(json.dumps(req_body))
    except:
        return handle_error('Request Failed: Could not write to storage.')

    # Trigger HTML Generator
    try:
        gen_url = 'https://' + os.getenv("WEBSITE_HOSTNAME") + '/api/htmlgenerator'
        payload = {'code': os.getenv("HTMLGENERATOR_KEY")}
        requests.get(gen_url, params=payload)
    except requests.exceptions.HTTPError as e:
        return handle_error("Request Failed: Invalid response code from html generator: " + e.response)
    except:
        return handle_error("Request Failed: Couldnt trigger html generator")

    push_notification("Success", "Record added at: " + str(datetime.now()))
    return func.HttpResponse("Success")
