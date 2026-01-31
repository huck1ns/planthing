import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PLANT_API_KEY")
BASE_URL = os.getenv("BASE_URL")

def searchAPI(query=None): 
    
    params = {
        'key': API_KEY
    }
    
    if query : 
        params['q'] = query

    try: 
        
        response = requests.get(BASE_URL, params = params)
        response.raise_for_status()
        
        data = response.json()
        
    
        return data
        
        
    except requests.exceptions.RequestException as e:
        print("Error searching API: {e}")
        return None
    
def parseAPI(data):
    plantData = []
    
    for plant in data.get('data', [])[:10]:
        filtered_data = {
            'common_name': plant.get('common_name'),
            'id': plant.get('id'),
            'scientific_name': plant.get('scientific_name')
        }
        
        plantData.append(filtered_data)
            
    return plantData
    
    
def userSearch(searchString):
    return parseAPI(searchAPI(searchString))





    


