# handler.py

import os


def hello(event, context):
    response = {
        "statusCode": 200,
        "body": "Hello from the {}!".format(os.environ.get('SERVICE_NAME'))
    }

    return response