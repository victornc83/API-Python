import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

def translate(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    
    translate = boto3.client(service_name='translate')
    
    item = {
        'id': result["Item"]["id"],
        'text': result["Item"]['text'],
        'checked': result["Item"]["checked"],
        'createdAt': result["Item"]["createdAt"],
        'updatedAt': result["Item"]["updatedAt"]
    }
    
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    
    return response