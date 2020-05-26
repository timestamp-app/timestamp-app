"""
This module contains notification functionality
"""
import logging
import os

import requests


# pylint: disable=W0702
def push_notification(code, message):
    """
    This function sends push notifications to a android device
    :param code:
    :param message:
    :return:
    """
    try:
        wirepusher_url = 'https://wirepusher.com/send'
        payload = {
            'id': os.getenv("WIREPUSHER_ID"),
            'title': 'Timestamp ' + code,
            'message': message,
            'type': code
        }
        requests.get(wirepusher_url, params=payload)
    except requests.exceptions.HTTPError as err:
        logging.error("Request Failed: Invalid response code from wirepusher: %s", err)
    except:
        logging.error("Request Failed: Couldnt trigger wirepusher")
