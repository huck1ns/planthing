import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Holder import Holder


app = QApplication(sys.argv)

window = Holder()
window.show()

app.exec()
