from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit
import API_Handler
from PySide6.QtCore import Qt



class Search_Window(QWidget):
    def __init__(self, logic):
        super().__init__()
        
        self.logic = logic
        self.setWindowTitle("Search Plant Database")
        self.resize(400,600)
        self.setMaximumSize(400,600)
        self.layout = QVBoxLayout()
        
        self.searchBar = QLineEdit()
        self.searchBar.setFixedHeight(30)
        self.layout.addWidget(self.searchBar)
        
        self.resultsList = Results(logic, self)
        self.searchBar.returnPressed.connect(self.searchPressed)
        self.layout.addWidget(self.resultsList)
        
        self.setLayout(self.layout)
        
    def searchPressed(self):
        userInput = self.searchBar.text()
        self.resultsList.search(userInput)
        
class Results(QWidget):
    
    def __init__(self, logic, window):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.logic = logic
        self.window = window
        
    def clearSearchPane(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
    def search(self, userInput):
        self.clearSearchPane()
        
        loadingLabel = QLabel("Searching database...")   
        self.layout.addWidget(loadingLabel, alignment = Qt.AlignCenter)
        
        
        results = API_Handler.userSearch(userInput)
        self.clearSearchPane()
        if len(results) == 0:
            noneLabel = QLabel("No results.")
            self.layout.addWidget(noneLabel, alignment = Qt.AlignCenter)
        
        resultsButtons = []
        
        for plant in results: 
            plantName = plant["common_name"]
            id = plant["id"]
            science = plant["scientific_name"]
            result = self.createResultButton(plantName, id, science)
            resultsButtons.append(result)
            
        for button in resultsButtons:
            self.layout.addWidget(button, alignment=Qt.AlignCenter)
            
        self.layout.addStretch()
        
        self.setLayout(self.layout)
            
        
        
    def createResultButton(self, plantName, plantID, science):
        capName = str(plantName).title()
        names = (capName+ "\n"+ str(science))
        result = QPushButton(names)
        result.setFixedSize(350, 47)
        
        #ID stored as property of the button
        result.setProperty("plant_id", plantID)
        
        result.clicked.connect(self.buttonPress)
        
        return result
    
    def buttonPress(self):
        #Retrieve the id of this instance of the button
        sender = self.sender()
        id = sender.property("plant_id")
        
        #Search and update
        plantData = API_Handler.buttonIDSearch(id)
        self.logic.updatePlant(plantData)
        self.window.close
        
        
        
        
    
        
        
        
        
        
        
        
        