import os
import sys
import json
import logging

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def translate(event, context):
    logger.info(event)
    
    try:
        table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
        result = table.get_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
        logger.info(result)
    except Exception as e:
        logger.error(e)
        raise Exception("[ErrorMessage]: " + str(e))   
        
    try:
        translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
        translated_text = translate.translate_text(Text=result["Item"]['text'], SourceLanguageCode="auto", TargetLanguageCode=event['pathParameters']['lang'])
        logger.info(translated_text)
    except Exception as e:
        logger.error(e)
        raise Exception("[ErrorMessage]: " + str(e))
    
    result["Item"]["text"] = translated_text["TranslatedText"]
    
    response = {
        "statusCode": 200,
        "body": json.dumps(result["Item"])
    }
    
    return response