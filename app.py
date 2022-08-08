import json
import requests

def handler(event, context):

    # TODO implementation
    
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "Your app from Container image has run via lambda!",
                            "event": event})
    }
