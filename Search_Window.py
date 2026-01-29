from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit
import API_Handler


class Search_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Plant Database")
        self.resize(400,600)
        layout = QVBoxLayout()
        
        self.searchBar = QLineEdit()
        self.searchBar.setFixedHeight(30)
        layout.addWidget(self.searchBar)
        self.searchBar.returnPressed.connect(self.search)
        layout.addStretch()
        
        self.setLayout(layout)
        
    
        
    def search(self):
        input = self.searchBar.text()
        results = API_Handler.userSearch(input)
        print(results)
        
        
        
        
        
        
        
        