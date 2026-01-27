from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QHBoxLayout, QStackedLayout, QSizePolicy
from PySide6.QtCore import Qt

class Display_Indicator(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.layout = QStackedLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    
        self.livingSVG = QSvgWidget('resources/livingplant.svg')
        self.deadSVG = QSvgWidget('resources/deadplant.svg')
        self.emptySVG = QSvgWidget('resources/noplant.svg')
        
        for svg in (self.livingSVG, self.deadSVG, self.emptySVG):
            svg.renderer().setAspectRatioMode(Qt.KeepAspectRatio)

        self.layout.addWidget(self.deadSVG)           # Dead in index 0
        self.layout.addWidget(self.livingSVG)         # Living in index 1
        self.layout.addWidget(self.emptySVG)          # Empty pot in index 2
        
        self.setToEmpty()
        
    def setToDead(self):
        self.layout.setCurrentIndex(0)
    
    def setToLiving(self):
        self.layout.setCurrentIndex(1)
    
    def setToEmpty(self):
        self.layout.setCurrentIndex(2)
        
    def swapImages(self):
        if self.layout.currentIndex() == 0:
            self.setToLiving()
        else: self.setToDead()
        
        
    
        