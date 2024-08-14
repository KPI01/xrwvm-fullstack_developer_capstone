# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
print("restapis.py backend_url:", backend_url)
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")
print("restapis.py sentiment_analyzer_url", sentiment_analyzer_url)


def get_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"
    request_url = backend_url+endpoint+"?"+params
    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        print("restapis.py response:", response)
        print("restapis.py response.json():", response.json())
        return response.json()

    except Exception as e:
        print(f"Network exception occurred [{e}]")


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    print("restapis.py request_url:", request_url)
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Network exception occurred [{e}]")


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred [{e}]")
