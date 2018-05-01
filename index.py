import json
import datetime
import requests


def handler(event, context):
    response = requests.get('http://www.mocky.io/v2/5ae856682d0000d2077b47dd',stream=True)

    contentType = response.headers['content-type']
    data = response.json()
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
