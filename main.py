import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Holder import Holder
from Plant import Plant
from App_Flow import Controller


app = QApplication(sys.argv)
controller = Controller()

window = controller.holder

window.setPlantName(controller.plant.plantName)

window.show()

app.exec()
