from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtCore import Qt
import os
import subprocess
import re
from bs4 import BeautifulSoup
class Controller:
    # ----Utilities----
    @classmethod
    def changeFont(cls, self):
        self.editor.setFontPointSize(int(self.fontSize.value()))
    
    @classmethod
    def addCustomFont(cls):
        fontPath = r"fonts"
        if os.path.exists(os.path.abspath(".") + os.sep + fontPath):
            for file in os.listdir(os.path.abspath(".") + os.sep + fontPath):
                if file.endswith(".ttf"):
                    QFontDatabase.addApplicationFont(fontPath.replace(os.sep, "/") + "/" + file)
    @classmethod
    def savePDF(cls, self):
        file, _ = QFileDialog.getSaveFileName(
            self, "Save PDF File", "", "Pdf Files (*.pdf);;All Files (*)")
        if file != "":
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file)
            self.editor.document().print_(printer)

    @classmethod
    def openPDF(cls, self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Open PDF File", "", "Pdf Files (*.pdf);;All Files (*)")
        if file != "" and file.endswith(".pdf"):
            msg = QMessageBox()
            msg.setWindowTitle("Loading PDF...")
            msg.setText("Loading....................................")
            msg.show()
            CREATE_NO_WINDOW = 0x08000000
            subprocess.call([r"pdf2htmlex\pdf2htmlEX.exe",
                             file, "--process-type3=1", "--optimize-text=1", "--correct-text-visibility=1", r"--data-dir=.\pdf2htmlex\data"], creationflags=CREATE_NO_WINDOW)
            fileName = file.split(os.altsep)[-1]
            fileName = fileName.replace(".pdf", ".html")
            with open(fileName, "r", encoding="utf-8") as f:
                parsedHtml = BeautifulSoup(f.read(), "html.parser")
                for tag in parsedHtml.find_all(["style", "script", "head"]):
                    tag.decompose()
                for tag in parsedHtml.find_all("div"):
                    if re.search(r"t\s([a-z]+\d+\s)+ls\d+", str(tag)) != None and re.search(r"^\d+$", tag.text) != None:
                        tag.decompose()
            self.editor.insertHtml(str(parsedHtml))
            os.remove(fileName)
            msg.close()

    @classmethod
    def changeFontSize(cls, self):
        if self.fontSize.value() != "" and int(self.fontSize.value()) > 0:
            self.editor.setFontPointSize(int(self.fontSize.value()))

    @classmethod
    def checkSize(cls, self):
        if self.editor.textCursor().position() == 0:
            self.editor.setFontPointSize(int(self.fontSize.value()))

    @classmethod
    def checkInfo(cls, self):
        text = self.editor.toPlainText()
        wordsCount = re.findall(r"\w+", text)
        charactersCount = re.findall(r"\w", text)
        self.wordsCounter.setText(str(len(wordsCount)))
        self.charactersCounter.setText(str(len(charactersCount)))

    # ----Text Editation----
    @classmethod
    def insertImage(cls, self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files(*.jpg, *.png);;All Files (*)")
        if file != "" and file.endswith(".jpg") or file.endswith(".png"):
            self.editor.insertHtml(f"<br><img src={file}></img>")

    @classmethod
    def alignCenter(cls, self):
        self.editor.setAlignment(Qt.AlignCenter) #type: ignore

    @classmethod
    def alignLeft(cls, self):
        self.editor.setAlignment(Qt.AlignLeft) #type: ignore

    @classmethod
    def alignRight(cls, self):
        self.editor.setAlignment(Qt.AlignRight) #type: ignore

    @classmethod
    def insertList(cls, self):
        cursor = self.editor.textCursor()
        cursor.insertHtml(f"<ul><li>{cursor.selectedText()}</li></ul>")
    
