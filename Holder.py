from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from Display_Indicator import Picture_Stack, Display_Indicator, Value_Pane
from PySide6.QtGui import QFont

class Holder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Planthing!")
        self.resize(800, 600)
        #self.setMinimumSize(800,600)
        #self.setMaximumSize(800,600)
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
        
        #vbox.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        vbox.addStretch()
        
        testImageButton = QPushButton("Press to change image")
        testImageButton.clicked.connect(self.imageDisplay.pictures.swapImages)
        vbox.addWidget(testImageButton, alignment=Qt.AlignCenter)
        
        layoutWidget = QWidget()
        
        layoutWidget.setLayout(vbox)
        
        
        self.setCentralWidget(layoutWidget)
        
        
    def setPlantName(self, name):
        combinedName = f"Plant name: {name}"
        self.plantNameLabel.setText(combinedName)
