import logging
import json

import azure.functions as func


def main(req: func.HttpRequest, recordsJSON):
    logging.info('HTML Generator function processed a request.')

    try:
        records = json.loads(recordsJSON)
    except:
        logging.error('Error reading records.')

    try:
        pass
    except:
        pass
