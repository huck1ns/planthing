from Holder import Holder
from Plant import Plant
from Search_Window import Search_Window



class Controller:
    def __init__(self):
        self.search = Search_Window(self)
        self.holder = Holder(self.search)
        self.plant = Plant.noArgPlant()
    
    def updatePlant(self, plantData):
        name = plantData["common_name"]
        watering = self.interpretWaterLevel(str(plantData["watering"]))
        light = self.interpretLightLevel(str(plantData["sunlight"]))
        
        self.plant = Plant(name, watering, light)
        self.holder.newPlant(self.plant)
        
        
        
        
    def interpretWaterLevel(self, des):
        des = des.lower()
        if des == "none": return 0
        if des == "minimum": return 1
        if des == "average": return 2
        if des == "frequent": return 3
        
    def interpretLightLevel(self, des):
        des = des.lower()
        if des == "full shade": return 0
        if des == "part shade": return 1
        if des == "sun-part shade": return 2
        if des == "full sun": return 3
        
        
        
        
    
        
        
        
    
        