import requests
import json
import dotenv
import os
dotenv.load_dotenv()
key = os.getenv("ACCESS_KEY")
def getImg():
    headers = {
        'Authorization': f'Client-ID {key}'
    }
    response = requests.get('https://api.unsplash.com/photos/random', headers=headers)
    data = response.json()
    return data['urls']['regular']
