from Holder import Holder
from Plant import Plant
from Search_Window import Search_Window
from Config_Manager import create_config, read_config
from pathlib import Path
from Device_Handler import Device_Handler
class Controller:
    def __init__(self):
        self.search = Search_Window(self)
        self.holder = Holder(self.search)
        self.device = Device_Handler()
        self.handle_config()
        while self.device.connection:
            self.interpret_sensors()
            
        
    
    def updatePlant(self, plantData):
        name = plantData["common_name"]
        watering = self.interpretWaterLevel(str(plantData["watering"]))
        light = self.interpretLightLevel(plantData["sunlight"])
        
        self.plant = Plant(name, watering, light)
        create_config(self)
        self.holder.newPlant(self.plant)
        
    def loadPlant(self):
        self.holder.newPlant(self.plant)
        
    """
    Takes string description for water level and converts it to 0-3 scale.
    """
    def interpretWaterLevel(self, des):
        des = des.lower()
        if des == "none": return 0
        if des == "minimum": return 1
        if des == "average": return 2
        if des == "frequent": return 3
        
    def interpretLightLevel(self, des):
        desc = des[0].lower()
        print(desc)
        level = 0
        for val in des:
            if val == "none": level += 0
            if val == "part shade": level += 1
            if val == "part sun/part shade": level += 3
            if val == "part sun": level += 2
            if val == "full sun": level += 4
        return level
        
    def handle_config(self):
        file_path = Path("config.ini")
        
        if file_path.exists():
            self.load_config()
        
        else:
            create_config(self)
            self.load_config()
        
        
    """
    Set current plant to one saved in config, runs once upon program start.
    """
    def load_config(self):
        NAME = 0
        WATER = 1
        LIGHT = 2
        
        plantDetails = read_config()
        self.plant = Plant(plantDetails[NAME], plantDetails[WATER], plantDetails[LIGHT])
        self.loadPlant()
        
    def interpret_sensors(self):
        stream = self.device.process_queue()
        water = int(stream[0])
        light = int(stream[3])
        
        
        #BAD PRACTICE, JUST TESTING!!!
        self.holder.indicator.values.waterUpdate(water)
        self.holder.indicator.values.lightUpdate(light)

        
        
        
        
        
        
        
        
        
    
        
        
        
    
        