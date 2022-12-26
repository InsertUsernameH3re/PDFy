# -*- coding: utf8 -*-
import PySimpleGUI
from findFonts import findFonts
from loadFonts import loadFonts
from changeFont import changeFont
from addImage import addImage
from savePDF import savePDF
from loadPDF import loadPDF

fontDir = "./fonts/"
fonts = loadFonts(findFonts(fontDir), fontDir)

def callbackOptionMenu(var, index, mode):
    window.write_event_value("Fonts", window['Fonts'].TKStringVar.get()) #type: ignore

buttons = [[PySimpleGUI.Button("Open"), PySimpleGUI.Button("Save"), PySimpleGUI.Button("Insert"), PySimpleGUI.OptionMenu(fonts, key="Fonts")]]
layout = [buttons,[PySimpleGUI.Multiline(size=(61, 95), key='Textbox', auto_refresh=True, autoscroll=True, font=("Arial", 15))]]
window = PySimpleGUI.Window('PDFy', layout, finalize=True, auto_size_buttons=True, auto_size_text=True, resizable=True, element_justification='c')

window['Fonts'].TKStringVar.trace("w", callbackOptionMenu) # type: ignore
window.maximize()

while True:
    try:
        event, values = window.read()  # type: ignore
        print(event, values)
        if event == PySimpleGUI.WIN_CLOSED or event == 'Cancel':
            break
        if event == "Insert":
            addImage(window)
        if event == "Open":
            loadPDF(window)
        if event == "Save":
            savePDF(values, fontDir)
        if event == "Fonts":
            changeFont(window, values)
    except Exception as e:
        print(e)

window.close()


