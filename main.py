import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Holder import Holder
from Plant import Plant


app = QApplication(sys.argv)
initialPlant = Plant.noArgPlant()

window = Holder()

window.setPlantName(initialPlant.plantName)

window.show()

app.exec()
