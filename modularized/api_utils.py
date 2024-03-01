import requests
import json

def get_bird_data(url):

    response = requests.get(url)
    response.raise_for_status() 
    return response.json()
