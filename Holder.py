from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from Display_Indicator import Display_Indicator

class Holder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Planthing!")
        self.resize(800, 600)
        vbox = QVBoxLayout()
        self.setMinimumSize(400,550)
        
        self.plantNameLabel = QLabel()
        self.imageDisplay = Display_Indicator()
        self.imageDisplay.setMaximumSize(200,500)
        
        
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        vbox.addWidget(self.plantNameLabel)
        vbox.addWidget(self.imageDisplay,1)
        
        
        layoutWidget = QWidget()
        
        layoutWidget.setLayout(vbox)
        
        self.setCentralWidget(layoutWidget)
        
        
    def setPlantName(self, name):
        combinedName = f"Plant name:  {name}"
        self.plantNameLabel.setText(combinedName)
        
        

        
        