import tableEditor_window
from PyQt5.QtWidgets import QMainWindow

class TableEditor(QMainWindow, tableEditor_window.Ui_tableEditor):
    def __init__(self, editor):
        self.editor = editor
        super().__init__()
        self.setupUi(self)
        self.create.pressed.connect(lambda: self.createTable())

    def createTable(self):
        rowsCount = self.rowsCounter.value()
        columnCount = self.columnCounter.value()
        padding = self.paddingCounter.value()
        tableName = self.tableName.text()
        if tableName != "":
            html = f"<table border=1 cellpadding={padding}><tr><th colspan={columnCount}>{tableName}</th></tr>"
        else:
            html = f"<table border=1 cellpadding={padding}>"
        for _ in range(rowsCount):
            html += "<tr>"
            for _ in range(columnCount):
                html += "<td></td>"
            html += "</tr>"
        html += "</table>"
        print(html)
        self.editor.insertHtml(html)
        self.close()
        
