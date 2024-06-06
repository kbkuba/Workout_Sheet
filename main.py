import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
EXCERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}


request_body = {
    "query": input("Tell me which exercises you did: "),
    "gender": "man",
    "weight_kg": 60,
    "height_cm": 180,
    "age": 23,
}
response = requests.post(url=EXCERCISE_ENDPOINT, json=request_body, headers=headers)
print(response.json())
result = response.json()

url = os.environ.get("SHEET_ENDPOINT")

today = datetime.now()

body = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%X"),
        "exercise": result["exercises"][0]["name"],
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"],
    }
}

auth = {
    "Authorization": os.environ.get("BASIC_AUTH")
}

sheet_input = requests.post(url=url, json=body, headers=auth)
print(sheet_input.json())

