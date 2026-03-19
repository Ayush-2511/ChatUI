import requests
import json
key = 'ntxElg9WFahbHrGfBbhxgRUuInAuHSi-6owgUKSjGlo'
def getImg():
    headers = {
        'Authorization': f'Client-ID {key}'
    }
    response = requests.get('https://api.unsplash.com/photos/random', headers=headers)
    data = response.json()
    return data['urls']['regular']
