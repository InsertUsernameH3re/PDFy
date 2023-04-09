import main_window
from controller import Controller
import merger
import tableEditor
import hyperlinkEditor
import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow)

html = "<a href=https://stackoverflow.com/questions/35858340/clickable-hyperlink-in-qtextedit>asdsad</a>"

class PDFy(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Merger = merger.Merger()
        self.TableEditor = tableEditor.TableEditor(self.editor)
        self.HyperLinkEditor = hyperlinkEditor.HyperlinkEditor(self.editor)
        self.editor.document().setDocumentMargin(120)

        #---Sockets--- 
        self.fontComboBox.currentFontChanged.connect(lambda: Controller.changeFont(self))
        self.save.triggered.connect(lambda: Controller.savePDF(self))
        self.open.triggered.connect(lambda: Controller.openPDF(self))
        self.insertImage.triggered.connect(lambda: Controller.insertImage(self))
        self.fontSize.setRange(5, 99)
        self.fontSize.valueChanged.connect(lambda: Controller.changeFontSize(self))
        self.editor.textChanged.connect(lambda: Controller.checkInfo(self))
        self.editor.textChanged.connect(lambda: Controller.checkSize(self))
        self.pdfMerger.triggered.connect(lambda: self.Merger.show())
        self.table.pressed.connect(lambda: self.TableEditor.show())
        self.hyperLink.pressed.connect(lambda: self.HyperLinkEditor.show())
        self.alignCenter.pressed.connect(lambda: Controller.alignCenter(self))
        self.alignLeft.pressed.connect(lambda: Controller.alignLeft(self))
        self.alignRight.pressed.connect(lambda: Controller.alignRight(self))
        self.list.pressed.connect(lambda: Controller.insertList(self))


if __name__ == "__main__":
    app = QApplication([])
    win = PDFy()
    win.show()
    sys.exit(app.exec())
