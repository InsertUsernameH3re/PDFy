from main_window import *
from controller import Controller
import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication, QMainWindow)

onlyInt = QIntValidator()
onlyInt.setRange(5, 99)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save.triggered.connect(lambda: Controller.savePDF(self))
        self.open.triggered.connect(lambda: Controller.openPDF(self))
        self.insertImage.triggered.connect(lambda: Controller.insertImage(self))
        self.fontSize.setValidator(onlyInt)
        self.fontSize.textEdited.connect(lambda: Controller.changeFontSize(self))
        self.editor.textChanged.connect(lambda: Controller.checkSize(self))
        

if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())
