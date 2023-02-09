from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QTextCursor
from PyQt5.QtPrintSupport import QPrinter
import fitz
import PyPDF2

class Controller:

        @classmethod
        def savePDF(cls, self):
            file = QFileDialog.getSaveFileName(self, 'Save PDF', None, '.pdf')
            if file[0] != "":
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(file[0] + file[1])
                self.editor.document().print_(printer)
        
        @classmethod
        def openPDF(cls, self):
            #file = QFileDialog.getOpenFileName(self, 'Save PDF', None, '.pdf')
            pdfReaderText = PyPDF2.PdfReader("hello.pdf")
            pdfReaderImages = fitz.open("hello.pdf")
            pdfText = ""
            pdfImage = ""
            for i in range(pdfReaderText.numPages):
                page = pdfReaderImages[i]
                print(page.get_images())

        @classmethod
        def changeFontSize(cls, self):
            if self.fontSize.text() != "" and int(self.fontSize.text()) > 0:
                self.editor.setFontPointSize(int(self.fontSize.text()))
    
        @classmethod
        def checkSize(cls, self):
            if self.editor.fontPointSize() != int(self.fontSize.text()):
                self.editor.setFontPointSize(int(self.fontSize.text()))

        @classmethod
        def insertImage(cls, self):
            file = QFileDialog.getOpenFileName(self, "Open Image", None, initialFilter="Image Files (*.png * .jpg * .bmp)")
            if file[0] != "":
                cursor = self.editor.textCursor()
                cursor.insertImage("mobileapp.png")
             
