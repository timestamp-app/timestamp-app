import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except:
        logging.info('Request Failed: No JSON input supplied.')
        return func.HttpResponse("Requires JSON input", status_code=400)

    return func.HttpResponse("Success")        
