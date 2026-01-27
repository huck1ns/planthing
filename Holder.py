from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from Display_Indicator import Display_Indicator
from PySide6.QtGui import QFont

class Holder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Planthing!")
        self.resize(800, 600)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        
        vbox = QVBoxLayout()
        vbox.setSpacing(40)
        vbox.setContentsMargins(0, 15, 0, 15)
        vbox.addStretch()
        
        
        self.plantNameLabel = QLabel()
        font = QFont("Cascadia Mono", 20)
        font.setBold(True)
        self.plantNameLabel.setFont(font)
        vbox.addWidget(self.plantNameLabel)

        
        self.imageDisplay = Display_Indicator()
        self.imageDisplay.setMaximumSize(200,500)
        vbox.addWidget(self.imageDisplay)
        
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        vbox.addStretch()
        
        testImageButton = QPushButton("Press to change image")
        testImageButton.clicked.connect(self.imageDisplay.swapImages)
        vbox.addWidget(testImageButton)
        
        layoutWidget = QWidget()
        
        layoutWidget.setLayout(vbox)
        
        
        self.setCentralWidget(layoutWidget)
        
        
    def setPlantName(self, name):
        combinedName = f"Plant name: {name}"
        self.plantNameLabel.setText(combinedName)
        
        
        

        
        