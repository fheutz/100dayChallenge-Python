import json
import requests 
import time

def lambda_handler(event, context):
    # Disable SSL Verify = false Warnings
    requests.packages.urllib3.disable_warnings()
    urls = event
    lambdaReturn = {
        "responses": []
    }
    for url in urls:
        start = time.time()
        r = requests.get(url, verify=False)
        end = time.time()
        response = {
            "statusCode":str(r.status_code),
            "requestTime":str(end-start)[0:5],
            "url":url
        }
        lambdaReturn["responses"].append(response)
    return {
        'statusCode': 200,
        'body': lambdaReturn
    }

