import PyPDF2
import merger_window
from PyQt5.QtWidgets import QFileDialog, QMainWindow
class Merger(QMainWindow, merger_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.select.clicked.connect(lambda: getFilePaths(self))
        self.merge.clicked.connect(lambda: merge(self))

        filepaths = []

        def getFilePaths(self):
            file, _ = QFileDialog.getOpenFileNames(
                self, "Open PDF Files", "", "Pdf Files (*.pdf);;All Files (*)")
            if len(file) > 1:
                self.labelProgress.setText("Loading files...")
                for file in file:
                    filepaths.append(file)
                self.labelProgress.setText("Files loaded successfully")

        def merge(self):
            progress = 0
            self.labelProgress.setText("Merging files")
            pdf_write = PyPDF2.PdfFileWriter()

            for path in filepaths:
                progress += 90 / len(filepaths)
                self.progress.setValue(progress)
                pdf_reader = PyPDF2.PdfFileReader(path)
                for page in range(pdf_reader.getNumPages()):
                    pdf_write.addPage(pdf_reader.getPage(page))

            with open("merged.pdf", "wb") as f:
                pdf_write.write(f)
            self.progress.setValue(100)
            self.labelProgress.setText("Output file: merged.pdf")
