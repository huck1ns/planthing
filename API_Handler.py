import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PLANT_API_KEY")
Base_URL = os.getenv("BASE_URL")

def searchAPI(query=None): 
    


    params = {
        'key': API_KEY
    }
    
    if query : 
        params['q'] = query

    try: 
        response = requests.get(Base_URL, params = params)
        response.raise_for_status()
        
        data = response.json()
        return data
        
    except requests.exceptions.RequestException as e:
        print("ERror searching API: {e}")
        return None
    
search = searchAPI('fern')

if search:
    print(json.dumps(search, indent = 2))        


