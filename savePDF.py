import fpdf
from tkinter import filedialog
filetypesPDF = (('PDF', '*.pdf'), ('Any file', '*'))


def savePDF(values, font, fontSize, fontDir):
    FPDF = fpdf.FPDF()
    file = filedialog.asksaveasfile(
        title='Save a file', initialdir='/', filetypes=filetypesPDF, defaultextension='.pdf')

    if file != None:
        temp = font.split(' ')
        font = ""
        for i in range(len(temp)):
            font += temp[i]
        FPDF.add_font(font, fname=fontDir+font+".ttf")
        FPDF.set_font(font, size=fontSize)
        FPDF.add_page()
        FPDF.multi_cell(190, txt=values["TextBox"])
        FPDF.output(file.name)
