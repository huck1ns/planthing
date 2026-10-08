import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PLANT_API_KEY")
BASE_URL = os.getenv("BASE_URL")
ID_URL = os.getenv("ID_URL")

REQUEST_DELAY = 1


"""
Searches API based on input string.

Args: 
    query (string), default = None for general search. String used to build lookup query. 
    
Returns:
    data: Results in JSON format

Raises: 
    Request exception
"""
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

"""Searches database based on Plant IDs. Used to get more data on one selected plant from user search.

Args:
    ID(int): database ID referencing each plant
    
Returns:
    data: Plant specific data in JSON
    
Raises: 
    RequestException
"""
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
    
"""
Converts raw JSON data of search results to list of dictionaries of plant common and scientific name, and ID.
For display of list of choices, saves space by not pulling all data for each plant, just what needs to be known.
Specific data is only saved for selected plant by searchID method.

Args:
    data(JSON): JSON format containing data on all plants from database (sliced to 10 results), pulled from search.
    
Returns:
    data: array of dictionaries of common_name, id, scientific_name for all plants
"""
def parseAPI(data):
    plantData = []
    
    for plant in data.get('data', [])[:10]:
        
        #API free tier only allows species data for plants ID 1-3000 !!
        
        #if int(plant.get('id')) > 3000: continue
        
        filtered_data = {
            'common_name': plant.get('common_name'),
            'id': plant.get('id'),
            'scientific_name': plant.get('scientific_name')
            
        }
        print(filtered_data)
        
        plantData.append(filtered_data)
    return plantData

"""
Parses JSON from searchID method after lookup of specific plant information.

Args: 
    data(JSON): list of all data of any given plant.

Returns:
    plantData: dictionary of data containing common_name, scientific_name, watering, and sunlight.


"""
def parseID(data):
    plantData = {
        'common_name': data.get('common_name'),
        'scientific_name': data.get('scientific_name'),
        'watering': data.get('watering'),
        'sunlight': data.get('sunlight')
    }
    return plantData

"""
Looks up data from user supplied search string supplied in search box.

Args:
    searchString(string): String entered into search textbox by user
    
Returns:
    List of top 10 results from searchAPI method parsed by parseAPI method
"""
def userSearch(searchString):
    return parseAPI(searchAPI(searchString))

"""
Searches database based on the ID of the plant selected by user from list of buttons. Returns 0 and prints error if ID is outside of range 0-3000,
free API tier does not allow queries past this range.

Args:
    id(int): ID from plant selected
    
Returns:
    Dictionary of plant data parsed from JSON from searchID method
"""

def buttonIDSearch(id):
    print(id)
    if id>3000:
        print("Plant falls outside of free tier range. Sorry!")
        return 0
    else: x =  parseID(searchID(id))
    return x



    


