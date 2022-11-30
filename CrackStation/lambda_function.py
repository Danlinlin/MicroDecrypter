import json
import boto3


def buildResponse(statusCode, shaHash, text):
    response = {}
    response['statusCode'] = statusCode
    response['headers'] = {}
    response['headers']['Content-Type'] = 'application/json'
    body = {}
    body[shaHash] = text
    response['body'] = json.dumps(body)
    return response


def decrypt(shahash):
    s3 = boto3.client('s3')
    response = s3.select_object_content(
        Bucket='mycrackstationbucket',
        Key='data.csv',
        ExpressionType='SQL',
        Expression=f"SELECT text FROM s3Object s WHERE s.shaHash = '{shahash}'",
        InputSerialization={'CSV': {"FileHeaderInfo": "Use"}},
        OutputSerialization={'JSON': {}},
    )
    for event in response['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            record = json.loads(records)
            return record['text'].strip()


def lambda_handler(event, context):
    response = {}
    if event['pathParameters'] is not None:
        shaHash = event['pathParameters']['shaHash']
        print("shaHash is", shaHash)
        res = decrypt(shaHash)
        print(res)
        if res is None:
            response = buildResponse(404, shaHash, "Password not found")
        else:
            response = buildResponse(200, shaHash, res)
    else:
        response = buildResponse(404, "Invalid input","Please input valid hash")

    return response