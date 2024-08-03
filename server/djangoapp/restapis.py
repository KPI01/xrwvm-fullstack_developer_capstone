# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params += key + "=" + value + "&"
    request_url = backend_url + endpoints + "?" + params

    print(f"GET from {request_url}")

    try:
        response = request.get(request_url)
        return response.json()
    except:
        print("Network exception ocurred")

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        reponse = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f'Unexpected {err=}, {type(err)=}')
        print("Network error ocurred")

def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception ocurred")
