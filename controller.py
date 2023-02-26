from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QTextCursor
from PyQt5.QtPrintSupport import QPrinter
import PyPDF2
class Controller:

        @classmethod
        def savePDF(cls, self):
            file, _ = QFileDialog.getSaveFileName(self, "Save PDF File", "", "Pdf Files (*.pdf);;All Files (*)")
            if file != "":
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(file)
                self.editor.document().print_(printer)
        
        @classmethod
        def openPDF(cls, self):
            file, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "Pdf Files (*.pdf);;All Files (*)")
            pdf_reader = PyPDF2.PdfFileReader(file)
            page = pdf_reader.getPage(0)
            self.editor.insertPlainText(page.extract_text())

        @classmethod
        def changeFontSize(cls, self):
            if self.fontSize.value() != "" and int(self.fontSize.value()) > 0:
                self.editor.setFontPointSize(int(self.fontSize.value()))
    
        @classmethod
        def checkSize(cls, self):
            print(self.editor.toHtml())
            if self.editor.fontPointSize() != int(self.fontSize.value()):
                self.editor.setFontPointSize(int(self.fontSize.value()))

        @classmethod
        def insertImage(cls, self):
            file, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files(*.jpg, *.png);;All Files (*)")
            if file[0] != "":
                cursor = self.editor.textCursor()
                cursor.insertImage(file)
#----------------------------------------------------PDF Merger------------------------------------------------------
        filepaths = []
        @classmethod
        def getFilePaths(cls, self):
            file, _ = QFileDialog.getOpenFileNames(self, "Open PDF Files", "", "Pdf Files (*.pdf);;All Files (*)")
            self.labelProgress.setText("Loading files...")
            for file in file:
                cls.filepaths.append(file)
            self.labelProgress.setText("Files loaded successfully")

        @classmethod
        def merge(cls, self):
            progress = 0
            self.labelProgress.setText("Merging files")
            pdf_write = PyPDF2.PdfFileWriter()

            for path in cls.filepaths:
                progress += 90 / len(cls.filepaths)
                self.progress.setValue(progress)
                pdf_reader = PyPDF2.PdfFileReader(path)
                for page in range(pdf_reader.getNumPages()):
                    pdf_write.addPage(pdf_reader.getPage(page))

            with open("merged.pdf", "wb") as f:
                pdf_write.write(f)
            self.progress.setValue(100)
            self.labelProgress.setText("Output file: merged.pdf")
#----------------------------------------------------------------------------------------------------------------------

