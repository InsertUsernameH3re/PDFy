# -*- coding: utf8 -*-
import PySimpleGUI
from PIL import Image, ImageTk
from tkinter import INSERT, filedialog
import PyPDF2
import fpdf

fontDir = "./fonts/"
filetypesPDF = (('PDF', '*.pdf'), ('Any file', '*'))
filetypesIMG = (('JPG', '*.jpg'), ('PNG', '.png'))
buttons = [[PySimpleGUI.Button("Open"), PySimpleGUI.Button("Save"), PySimpleGUI.Button("Insert")]]

layout = [buttons,[PySimpleGUI.Multiline(size=(61, 95), key='textbox', auto_refresh=True, autoscroll=True, font=("Arial", 15))]]

window = PySimpleGUI.Window('PDFy', layout, finalize=True, auto_size_buttons=True, auto_size_text=True, resizable=True, element_justification='c')
window.maximize()

def addImage(window):
    text = window['textbox'].widget
    global image
    img = filedialog.askopenfilename(title="Add Image", initialdir="/", filetypes=filetypesIMG, defaultextension=".png")
    img = Image.open(img)
    window["textbox"].update("//image//")
    image = ImageTk.PhotoImage(img)
    position = text.index(INSERT)
    text.image_create(position, image=image)

def save(values):
    FPDF = fpdf.FPDF()
    file = filedialog.asksaveasfile(
        title='Save a file', initialdir='/', filetypes=filetypesPDF, defaultextension='.pdf')

    if file != None:
        FPDF.add_font(fname=fontDir + "DejaVuSansCondensed.ttf")
        FPDF.set_font("DejaVuSansCondensed", size=15)
        FPDF.add_page()
        FPDF.multi_cell(190, txt=values["textbox"])
        FPDF.output(file.name)


def load(window):
    file = filedialog.askopenfilename(
        title='Open a file', initialdir='/', filetypes=filetypesPDF, defaultextension='.pdf')
    pdfReader = PyPDF2.PdfReader(file)
    pdfText = ""
    for i in range(pdfReader.numPages):
        page = pdfReader.getPage(i)
        pdfText += page.extract_text()
    window["textbox"].update(value=pdfText)


while True:
    try:
        event, values = window.read()  # type: ignore
        print(event, values)
        if event == PySimpleGUI.WIN_CLOSED or event == 'Cancel':
            break
        if event == "Insert":
            addImage(window)
        if event == "Open":
            load(window)
        if event == "Save":
            save(values)
    except:
        print("error")
window.close()
