import logging

import azure.functions as func


def main(req: func.HttpRequest, inputblob: func.InputStream) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    folder = req.route_params.get('folder')
    filename = req.route_params.get('filename')

    if folder and filename:
        return func.HttpResponse(body=inputblob.read(size=-1).decode('utf-8'),
                                status_code=200)

    else:
        return func.HttpResponse(
             "Please pass a folder and filename on the query string or in the request body",
             status_code=400
        )
