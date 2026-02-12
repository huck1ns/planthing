from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from Display_Indicator import Display_Indicator
from PySide6.QtGui import QFont
from Search_Window import Search_Window

class Holder(QMainWindow):
    def __init__ (self, search):
        super().__init__()
        
        #Initialize basic window properties
        self.setWindowTitle("Planthing!")
        self.resize(500, 750)
        self.setFixedSize(500, 750)
        self.setStyleSheet("QMainWindow { background-color: #F6FCF3; }")
        
        vbox = QVBoxLayout()
        vbox.setSpacing(40)
        vbox.setContentsMargins(0, 15, 0, 15)
        vbox.addStretch()
        
        self.search = search
        
        
        self.plantNameLabel = QLabel()
        font = QFont("Constantia", 20)
        font.setBold(True)
        self.plantNameLabel.setFont(font)
        self.plantNameLabel.setStyleSheet("color: #1A3028; padding-top: 20px")
        vbox.addWidget(self.plantNameLabel, alignment=Qt.AlignCenter)
        
        self.indicator = Display_Indicator()
        self.indicator.setMaximumSize(200,500)
        vbox.addWidget(self.indicator, alignment=Qt.AlignCenter)
        
        self.searchWindow = None
        
        #vbox.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        vbox.addStretch()
        
        searchButton = QPushButton("Search database")
        searchButton.setStyleSheet("""
            QPushButton {
                background-color: #3C7A5E;
                min-width: 200px;
                min-height: 50px;
                font-size: 14px;
            }
        """)
        searchButton.clicked.connect(self.showSearchWindow)
        vbox.addWidget(searchButton, alignment=Qt.AlignCenter)
        
        layoutWidget = QWidget()
        
        layoutWidget.setLayout(vbox)
        
        
        self.setCentralWidget(layoutWidget)
        
        
    def setPlantName(self, name):
        combinedName = f"Your Plant: {name}"
        self.plantNameLabel.setText(combinedName)
        
    def showSearchWindow(self):
        if self.searchWindow is None:
            self.searchWindow = self.search
        
        self.searchWindow.show()
        
    def newPlant(self, plant):
        self.setPlantName(plant.plantName)
        self.indicator.update(plant.exWaterLevel, plant.exLightLevel)
        self.indicator.pictures.setToLiving()
    
    
        
