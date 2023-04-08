import hyperlinkEditor_window
from PyQt5.QtWidgets import QMainWindow

class HyperlinkEditor(QMainWindow, hyperlinkEditor_window.Ui_hyperlinkEditor):
    def __init__(self, editor):
        self.editor = editor
        super().__init__()
        self.setupUi(self)
        self.create.pressed.connect(lambda: self.createHyperlink())
        self.hyperlink.textChanged.connect(lambda: self.textChanged())

    def textChanged(self):
        if len(self.text.text()) == 0:
            self.text.setText(self.hyperlink.text())

    def createHyperlink(self):
        if len(self.hyperlink.text()) != 0 and len(self.text.text()) != 0:
            self.editor.insertHtml(f"<a href={self.hyperlink.text()}>{self.text.text()}</a>")
            self.close()
