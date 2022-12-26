import fpdf
from tkinter import filedialog
filetypesPDF = (('PDF', '*.pdf'), ('Any file', '*'))
def savePDF(values, fontDir):
    FPDF = fpdf.FPDF()
    file = filedialog.asksaveasfile(
        title='Save a file', initialdir='/', filetypes=filetypesPDF, defaultextension='.pdf')

    if file != None:
        FPDF.add_font(fname=fontDir + "DejaVuSansCondensed.ttf")
        FPDF.set_font("DejaVuSansCondensed", size=15)
        FPDF.add_page()
        FPDF.multi_cell(190, txt=values["Textbox"])
        FPDF.output(file.name)
