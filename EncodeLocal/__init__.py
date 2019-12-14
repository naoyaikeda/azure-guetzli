import pyguetzli
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    from_path = req.params.get('from_path')
    to_path = req.params.get('to_path')
    if (not from_path) or (not to_path):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            from_path = req_body.get('from_path')
            to_path = req_body.get('to_path')

    if from_path:
        return func.HttpResponse(f"Hello {from_path}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
