import requests
import json

parameters={
    "amount":10,
    "category":20,
    "type":"boolean"
}


# api="https://opentdb.com/api.php?amount=10&category=20&type=boolean"
response=requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
question_data=response.json()["results"]