import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PLANT_API_KEY")
BASE_URL = os.getenv("BASE_URL")
ID_URL = os.getenv("ID_URL")

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
        print(f"Error searching API: {e}")
        return None
    
def searchID(id):
    params = {
        'key': API_KEY
    }
    
    try: 
        url = (ID_URL + str(id))
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error searching API: {e}")
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

def parseID(data):
    plantData = {
        'common_name': data.get('common_name'),
        'scientific_name': data.get('scientific_name'),
        'watering': data.get('watering'),
        'sunlight': data.get('sunlight')
    }
    print (plantData)
    return plantData
    


    
    
    
def userSearch(searchString):
    return parseAPI(searchAPI(searchString))

def buttonIDSearch(id):
    return parseID(searchID(id))




buttonIDSearch(2)
    


