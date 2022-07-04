import json

CORS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Credentials': True,
}

def say_hello():

    return {
        "statusCode": 200,
        "headers": CORS,
        "body": json.dumps({
            "message": "hello"
        })
    }