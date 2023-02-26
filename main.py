import main_window
import merger
from controller import Controller
import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow)

html = "<h3>Table</h3><table border=1><tr><th>Company</th><th>Contact</th><th>Country</th></tr><tr><td>Alfreds Futterkiste</td><td>Maria Anders</td><td>Germany</td></tr><tr><td>Centro comercial Moctezuma</td><td>Francisco Chang</td><td>Mexico</td></tr><tr><td>Ernst Handel</td><td>Roland Mendel</td><td>Austria</td></tr><tr><td>Island Trading</td><td>Helen Bennett</td><td>UK</td></tr><tr><td>Laughing Bacchus Winecellars</td><td>Yoshi Tannamuri</td><td>Canada</td></tr><tr><td>Magazzini Alimentari Riuniti</td><td>Giovanni Rovelli</td><td>Italy</td></tr></table>"

class Editor(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save.triggered.connect(lambda: Controller.savePDF(self))
        self.open.triggered.connect(lambda: Controller.openPDF(self))
        self.insertImage.triggered.connect(lambda: Controller.insertImage(self))
        self.fontSize.setRange(5, 99)
        self.fontSize.valueChanged.connect(lambda: Controller.changeFontSize(self))
        self.editor.textChanged.connect(lambda: Controller.checkSize(self))
        self.Merger = Merger()
        self.merger.triggered.connect(lambda: self.Merger.show())
        
class Merger(QMainWindow, merger.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.select.clicked.connect(lambda: Controller.getFilePaths(self))
        self.merge.clicked.connect(lambda: Controller.merge(self))

if __name__ == "__main__":
    app = QApplication([])
    win = Editor()
    win.show()
    sys.exit(app.exec())
