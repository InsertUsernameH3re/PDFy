from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtPrintSupport import QPrinter
import PyPDF2
import os
import subprocess
import re
from bs4 import BeautifulSoup
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
            if file != "":
                msg = QMessageBox()
                msg.setWindowTitle("Loading PDF...")
                msg.setText("Loading....................................")
                msg.show()
                subprocess.call([r"pdf2htmlex\pdf2htmlEX.exe",
                                 file, "--process-type3=1", "--optimize-tex=1", "--correct-text-visibility=1", r"--data-dir=pdf2htmlex\data"])
                fileName = file.split(os.altsep)[-1]
                fileName = fileName.replace(".pdf", ".html")
                with open(fileName, "r", encoding="utf-8") as f:
                    parsedHtml = BeautifulSoup(f.read(), "html.parser")
                    for tag in parsedHtml.find_all(["style", "script", "head"]):
                        tag.decompose()
                    for tag in parsedHtml.find_all("div", {"class": "t m0 x3 h3 y3 ff1 fs0 fc0 sc0 ls0"}):
                        tag.decompose()
                    for tag in parsedHtml.find_all("div", {"class": "t m0 x2 h2 y2 ff1 fs0 fc0 sc0 ls0"}):
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


        @classmethod
        def insertImage(cls, self):
            file, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files(*.jpg, *.png);;All Files (*)")
            if file != "":
                self.editor.insertHtml(f"<img src={file}></img>")
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

