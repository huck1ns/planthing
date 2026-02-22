from Holder import Holder
from Plant import Plant
from Search_Window import Search_Window
from Config_Manager import create_config, read_config
from pathlib import Path
class Controller:
    def __init__(self):
        self.search = Search_Window(self)
        self.holder = Holder(self.search)
        self.handle_config()
        
    
    def updatePlant(self, plantData):
        name = plantData["common_name"]
        watering = self.interpretWaterLevel(str(plantData["watering"]))
        light = self.interpretLightLevel(plantData["sunlight"])
        
        self.plant = Plant(name, watering, light)
        create_config(self)
        self.holder.newPlant(self.plant)
        
    def loadPlant(self):
        self.holder.newPlant(self.plant)
        
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
        
    def load_config(self):
        plantDetails = read_config()
        
        self.plant = Plant(plantDetails[0], plantDetails[1], plantDetails[2])
        self.loadPlant()
        
        
        
        
        
        
        
        
    
        
        
        
    
        