import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Holder import Holder
from Plant import Plant


app = QApplication(sys.argv)
userPlant = Plant.noArgPlant()

window = Holder()

window.setPlantName(userPlant.plantName)

window.show()

app.exec()
