from PyQt5 import QtWidgets

class Editor(QtWidgets.QTextEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    def dragEnterEvent(self, event):
        event.accept() if event.mimeData().hasText() else event.ignore()

    def dragMoveEvent(self, event):
        event.accept() if event.mimeData().hasText() else event.ignore()

    def dropEvent(self, event):
        data = str(event.mimeData().text())
        if data.startswith("file"):
            if data.endswith(".png") or data.endswith(".jpg"):
                self.insertHtml(f"<img src={event.mimeData().text()}></img>")
            else:
                self.insertPlainText(data)
        else:
            self.insertPlainText(data)
