"""
This module contains functionality for handling errors
"""
import logging

import azure.functions as func

from helpers.notifications import push_notification


def handle_error(message, code=500):
    """
    This function logs errors and sends a notification
    :param message:
    :param code:
    :return:
    """
    logging.error(message)
    push_notification("Error", message)
    return func.HttpResponse(message, status_code=code)
