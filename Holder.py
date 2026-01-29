from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from Display_Indicator import Display_Indicator
from PySide6.QtGui import QFont
from Search_Window import Search_Window

class Holder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Planthing!")
        self.resize(800, 600)
        self.setStyleSheet("QMainWindow { background-color: #162c3d; }")
        
        vbox = QVBoxLayout()
        vbox.setSpacing(40)
        vbox.setContentsMargins(0, 15, 0, 15)
        vbox.addStretch()
        
        
        self.plantNameLabel = QLabel()
        font = QFont("Cascadia Mono", 20)
        font.setBold(True)
        self.plantNameLabel.setFont(font)
        vbox.addWidget(self.plantNameLabel, alignment=Qt.AlignCenter)
        
        self.imageDisplay = Display_Indicator()
        self.imageDisplay.setMaximumSize(200,500)
        vbox.addWidget(self.imageDisplay, alignment=Qt.AlignCenter)
        
        self.searchWindow = None
        
        #vbox.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        vbox.addStretch()
        
        searchButton = QPushButton("Search database")
        searchButton.clicked.connect(self.showSearchWindow)
        vbox.addWidget(searchButton, alignment=Qt.AlignCenter)
        
        layoutWidget = QWidget()
        
        layoutWidget.setLayout(vbox)
        
        
        self.setCentralWidget(layoutWidget)
        
        
    def setPlantName(self, name):
        combinedName = f"Plant name: {name}"
        self.plantNameLabel.setText(combinedName)
        
    def showSearchWindow(self):
        if self.searchWindow is None:
            self.searchWindow = Search_Window()
        
        self.searchWindow.show()
