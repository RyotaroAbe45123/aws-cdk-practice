import sys

import requests

def handler(event, context):
    return 'Hello from AWS Lambda using Python' + sys.version + '!'        