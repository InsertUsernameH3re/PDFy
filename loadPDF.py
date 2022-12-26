from tkinter import filedialog
import PyPDF2
filetypesPDF = (('PDF', '*.pdf'), ('Any file', '*'))
def loadPDF(window):
    file = filedialog.askopenfilename(
        title='Open a file', initialdir='/', filetypes=filetypesPDF, defaultextension='.pdf')
    pdfReader = PyPDF2.PdfReader(file)
    pdfText = ""
    for i in range(pdfReader.numPages):
        page = pdfReader.getPage(i)
        pdfText += page.extract_text()
    window["Textbox"].update(value=pdfText)
