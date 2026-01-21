from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class Holder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Planthing!")
        self.resize(800, 600)
        vbox = QVBoxLayout()
        
        plantName = QLabel("Your Plant: ")
        vbox.addWidget(plantName)
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        
        layoutWidget = QWidget()
        
        layoutWidget.setLayout(vbox)
        
        self.setCentralWidget(layoutWidget)
        
        