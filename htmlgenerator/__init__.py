import logging
import json

import azure.functions as func

from . import generator


def main(req: func.HttpRequest, recordsJSON):
    logging.info('HTML Generator function processed a request.')

    try:
        records = json.loads(recordsJSON)
    except:
        logging.error('Error reading records.')

    gen = generator.generator(records)
    gen.make_html()
