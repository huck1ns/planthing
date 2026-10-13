from Holder import Holder
from Plant import Plant
from Search_Window import Search_Window
from Config_Manager import create_config, read_config
from pathlib import Path
from Device_Handler import Device_Handler
from PySide6.QtCore import QTimer

class Controller:
    def __init__(self):
        self.search = Search_Window(self)
        self.holder = Holder(self.search)
        self.device = Device_Handler()
        self.handle_config()
        self.holder.updateConnectionStatus(self.device.connection)
        if self.device.connection:
            self.interpret_sensors()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    
    """
    Ran on 1 second timer to provide constant GUI updates to sensor readings and ensure that device is connected.
    """
    def update(self):
        self.holder.updateConnectionStatus(self.device.checkConnection())
        self.interpret_sensors()
    
    
    """
    Creates a new plant, overwriting the previous, with user selected plant to update desired levels.

    Args: 
    plantData: dictionary of plant common_name, watering, and sunlight
    """
    def updatePlant(self, plantData):
        name = plantData["common_name"]
        watering = self.interpretWaterLevel(str(plantData["watering"]))
        light = self.interpretLightLevel(plantData["sunlight"])
        
        self.plant = Plant(name, watering, light)
        create_config(self)
        self.holder.newPlant(self.plant)
        
    """
    Update GUI with current plant data.
    """
    def loadPlant(self):
        self.holder.newPlant(self.plant)
        
    """
    Take string description for water level and convert it to 0-3 scale.
    
    Args: 
        des: description of water level
    """
    def interpretWaterLevel(self, des):
        des = des.lower()
        if des == "none": return 0
        if des == "minimum": return 1
        if des == "average": return 2
        if des == "frequent": return 3
    
    """
    Take string description for light level and convert it to 0-3 scale.
    
    Args: 
        des: description of light level
    """
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
        
    """Load saved data from past use or create a config if it has been removed / first time running."""
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
        
    """Read from sensor data to update light and water, update to zeroes if there is no data. """
    def interpret_sensors(self):
        stream = self.device.process_queue()
        water = 0
        light = 0
        if stream is not None: 
            water = int(stream[0])
            light = int(stream[2])
        
        self.holder.indicator.values.waterUpdate(water)
        self.holder.indicator.values.lightUpdate(light)

        
        
        
        
        
        
        
        
        
    
        
        
        
    
        