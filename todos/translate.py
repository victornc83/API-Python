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
    translated_text = translate.translate_text(Text=result["Item"]['text'], SourceLanguageCode="auto", TargetLanguageCode=event['pathParameters']['lang'])
    
    item = {
        'id': result["Item"]["id"],
        'text': translated_text,
        'checked': result["Item"]["checked"],
        'createdAt': result["Item"]["createdAt"],
        'updatedAt': result["Item"]["updatedAt"]
    }
    
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    
    return response