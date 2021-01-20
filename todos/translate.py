import json
import boto3
#dynamodb = boto3.resource('dynamodb')




#import boto3
def translate(event, context):
    data = json.loads(event['body'])
    translate = boto3.client('translate')
    result = translate.translate_text(Text=data['text'],
                                      SourceLanguageCode=data['idiomaO'],
                                      TargetLanguageCode=data['idiomaD'])

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result["TranslatedText"])
    }

    return response