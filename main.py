import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Holder import Holder
from Plant import Plant
from App_Flow import Controller

"""

Script for initializing app.

Controller is class that handles the flow of application logic.

Holder is container for all GUI aspects, assigned to main window.

"""

app = QApplication(sys.argv)
controller = Controller()

window = controller.holder

window.show()

app.exec()
