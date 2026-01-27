from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QHBoxLayout

class Display_Indicator(QWidget):
    def __init__(self):
        central_widget = self
        super().__init__()
        
        
        layout = QHBoxLayout()
        svg_widget = QSvgWidget('resources/livingplant.svg')
        svg_widget.resize(100,400)
        
        layout.addWidget(svg_widget)
        central_widget.setLayout(layout)
        