from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QHBoxLayout, QStackedLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class Picture_Stack(QWidget):
    def __init__(self):
        super().__init__()
        
        #Pictures
        self.pictures = QStackedLayout(self)
        self.pictures.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    
        self.livingSVG = QSvgWidget('resources/livingplant.svg')
        self.deadSVG = QSvgWidget('resources/deadplant.svg')
        self.emptySVG = QSvgWidget('resources/noplant.svg')
        
        for svg in (self.livingSVG, self.deadSVG, self.emptySVG):
            svg.renderer().setAspectRatioMode(Qt.KeepAspectRatio)

        self.pictures.addWidget(self.deadSVG)           # Dead in index 0
        self.pictures.addWidget(self.livingSVG)         # Living in index 1
        self.pictures.addWidget(self.emptySVG)          # Empty pot in index 2
        
        self.setToEmpty()
        
    def setToDead(self):
        self.pictures.setCurrentIndex(0)
    
    def setToLiving(self):
        self.pictures.setCurrentIndex(1)
    
    def setToEmpty(self):
        self.pictures.setCurrentIndex(2)
        
    def swapImages(self):
        nextIndex = (self.pictures.currentIndex()+1)%3
        self.pictures.setCurrentIndex(nextIndex)
        
class Value_Pane(QWidget):
    def __init__(self):
        super().__init__()
        
        # self.container = QWidget(self)
        # self.container.setObjectName("background")
        
        self.textBox = QVBoxLayout()
        #self.container.setLayout(self.textBox)
        self.setLayout(self.textBox)
        # self.setStyleSheet("#background {background-color: #3C7A5E; border-radius: 10px; }")
        self.setStyleSheet("background-color: #3C7A5E; border-radius: 10px; ")
        #self.textBox.setSpacing(0)
        self.textBox.addStretch()
        
        self.waterLabel = QLabel()
        self.waterLabel.setStyleSheet("padding-left: 5px; padding-right: 5px; padding-top:8px; padding-bottom: 1px;")
        self.waterExpectationLabel = QLabel()
        self.waterExpectationLabel.setStyleSheet("padding-left: 5px; padding-right: 5px; padding-top:1px; padding-bottom: 8px;")
        self.waterUpdate("0")
        
        self.lightLabel = QLabel()
        self.lightLabel.setStyleSheet("padding-left: 5px; padding-right: 5px; padding-top:8px; padding-bottom: 1px;")
        self.lightExpectationLabel = QLabel()
        self.lightExpectationLabel.setStyleSheet("padding-left: 5px; padding-right: 5px; padding-top:1px; padding-bottom: 8px;")
        self.lightUpdate("0")
        
        self.textBox.addWidget(self.waterLabel)
        self.textBox.addWidget(self.waterExpectationLabel)
        self.textBox.addWidget(self.lightLabel)
        self.textBox.addWidget(self.lightExpectationLabel)
        self.textBox.addStretch()
        
    def updateExpectations(self, water, light):
        water_exp = f"Expected Water Level: {water}"
        self.waterExpectationLabel.setText(water_exp)
        
        light_exp = f"Expected Light Level: {light}"
        self.lightExpectationLabel.setText(light_exp)
        
    def waterUpdate(self, waterLevel):
        WATER_TEXT = f"Current Water Level: {waterLevel}"
        self.waterLabel.setText(WATER_TEXT)
        
        
    def lightUpdate(self, lightLevel):
        LIGHT_TEXT = f"Current Light Level: {lightLevel}"
        
        
        self.lightLabel.setText(LIGHT_TEXT)
        
        
        
class Display_Indicator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QHBoxLayout(self)
        
        self.pictures = Picture_Stack()
        self.values = Value_Pane()
        
        self.layout.addWidget(self.pictures, 1)
        self.layout.addWidget(self.values, 1)
        
        
        
        self.setFixedWidth(400)
        
    def update(self, water, light):
        self.values.updateExpectations(water, light)
    
        