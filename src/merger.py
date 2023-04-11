import PyPDF2
import merger_window
from PyQt5.QtWidgets import QFileDialog, QMainWindow
class Merger(QMainWindow, merger_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.select.pressed.connect(lambda: self.getFilePaths())
        self.merge.pressed.connect(lambda: self.Merge())

        self.filepaths = []

    def getFilePaths(self):
        file, _ = QFileDialog.getOpenFileNames(
            self, "Open PDF Files", "", "Pdf Files (*.pdf);;All Files (*)")
        if len(file) > 1:
            self.labelProgress.setText("Loading files...")
            for file in file:
                self.filepaths.append(file)
            self.labelProgress.setText("Files loaded successfully")

    def Merge(self):
        progress = 0
        self.progress.setValue(progress)
        self.labelProgress.setText("Merging files")
        pdf_write = PyPDF2.PdfWriter()

        for path in self.filepaths:
            progress += 90 // len(self.filepaths)
            self.progress.setValue(progress)
            pdf_reader = PyPDF2.PdfReader(path)
            for page in range(len(pdf_reader.pages)):
                pdf_write.add_page(pdf_reader.pages[page])

        with open("merged.pdf", "wb") as f:
            pdf_write.write(f)
        self.progress.setValue(100)
        self.labelProgress.setText("Output file: merged.pdf")
