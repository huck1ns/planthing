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
        
        self.textBox = QVBoxLayout(self)
        self.textBox.setSpacing(0)
        self.textBox.addStretch()
        
        self.waterLabel = QLabel()
        self.waterExpectationLabel = QLabel()
        self.waterUpdate("0", "0")
        
        self.lightLabel = QLabel()
        self.lightExpectationLabel = QLabel()
        self.lightUpdate("0", "0")
        
        self.textBox.addWidget(self.waterLabel)
        self.textBox.addWidget(self.waterExpectationLabel)
        self.textBox.addSpacing(20)
        self.textBox.addWidget(self.lightLabel)
        self.textBox.addWidget(self.lightExpectationLabel)
        self.textBox.addStretch()
        
    def waterUpdate(self, waterLevel, expected):
        WATER_TEXT = f"Current Water Level: {waterLevel}"
        EXPECTATION = f"Expected Water Level: {expected}"
        
        self.waterLabel.setText(WATER_TEXT)
        self.waterExpectationLabel.setText(EXPECTATION)
        
    def lightUpdate(self, lightLevel, expected):
        LIGHT_TEXT = f"Current Light Level: {lightLevel}"
        EXPECTATION = f"Expected Light Level: {expected}"
        
        self.lightLabel.setText(LIGHT_TEXT)
        self.lightExpectationLabel.setText(EXPECTATION)
        
        
class Display_Indicator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QHBoxLayout(self)
        
        self.pictures = Picture_Stack()
        self.values = Value_Pane()
        
        self.layout.addWidget(self.pictures, 1)
        self.layout.addWidget(self.values, 1)
        
        self.setFixedWidth(400)
    
        