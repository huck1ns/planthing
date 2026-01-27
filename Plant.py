
LIGHT_DEVIATION = 0.5
WATER_DEVIATION = 0.5

class Plant():
    
    def __init__(self, name, waterLevel, lightLevel):
        self.plantName = name
        self.exWaterLevel = waterLevel
        self.exLightLevel = lightLevel
        
    @classmethod
    def noArgPlant(cls):
        return cls("None", 0, 0)
        
    
    def compareLight(self, lightLevel):
        dif = abs(self.exLightLevel-lightLevel) < LIGHT_DEVIATION
        if (dif < WATER_DEVIATION):
            return 1
        if (dif > WATER_DEVIATION):
            return -1
        
    def compareWater(self, waterLevel):
        dif = abs(self.exWaterLevel-waterLevel) < WATER_DEVIATION
        if (dif < WATER_DEVIATION):
            return 1
        if (dif > WATER_DEVIATION):
            return -1
        
        
        
        
        
        