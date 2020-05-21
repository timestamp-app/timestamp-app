"""
This module is responsible for ingesting data and writing it to storage
"""
import json
import logging
import os
from datetime import datetime
from uuid import uuid4

import azure.functions as func
import requests

from helpers.error_handling import handle_error
from helpers.notifications import push_notification


def format_input(data):
    """
    This function formats the input data to be written into th table
    :param data:
    :return:
    """
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


# pylint: disable=E1136,W0702
def main(req: func.HttpRequest, storageout: func.Out[str]) -> func.HttpResponse:
    """
    This function takes in a http request, formats the data, and writes it to storage
    :param req:
    :param storageout:
    :return:
    """
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
        storageout.set(json.dumps(req_body))
    except:
        return handle_error('Request Failed: Could not write to storage.')

    # Trigger HTML Generator
    try:
        gen_url = 'https://' + os.getenv("WEBSITE_HOSTNAME") + '/api/htmlgenerator'
        payload = {'code': os.getenv("HTMLGENERATOR_KEY")}
        requests.get(gen_url, params=payload)
    except requests.exceptions.HTTPError as err:
        return handle_error("Request Failed: Invalid response code from html generator: " + err)
    except:
        return handle_error("Request Failed: Couldnt trigger html generator")

    push_notification("Success", "Record added at: " + str(datetime.now()))
    return func.HttpResponse("Success")
