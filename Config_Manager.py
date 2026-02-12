import configparser

config = configparser.ConfigParser()

def create_config(controller, filename='config.ini'):
    
    plantName = controller.plant.plantName
    plantWater = str(controller.plant.exWaterLevel)
    plantLight = str(controller.plant.exLightLevel)
    
    
    config['Plant'] = {
        'name' : plantName,
        'water' : plantWater,
        'light' : plantLight
    }
    
    with open(filename, 'w') as configfile:
        config.write(configfile)
        
def read_config(filename='config.ini'):
    config.read(filename)
    
    name = config['Plant']['name']
    water = config['Plant']['water']
    light = config['Plant']['light']
    
    return (name, water, light)
    
    