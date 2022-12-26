# -*- coding: utf8 -*-
import PySimpleGUI
from findFonts import findFonts
from loadFonts import loadFonts
from changeFont import changeFont
from changeFontSize import changeFontSize
from addImage import addImage
from savePDF import savePDF
from loadPDF import loadPDF
import sys
import os

fontDir = getattr(sys, '_MEIPASS', os.path.dirname(__file__)) + "/fonts/"
fonts = loadFonts(findFonts(fontDir), fontDir)


def callbackOptionMenu(var, index, mode):
    window.write_event_value(
        "Fonts", window['Fonts'].TKStringVar.get())  # type: ignore


def callbackInput(var, index, mode):
    window.write_event_value(
        "FontSize", window['FontSize'].TKStringVar.get())  # type: ignore


buttons = [[PySimpleGUI.Button("Open"), PySimpleGUI.Button("Save"), PySimpleGUI.Button("Insert"), PySimpleGUI.Text("Font:"), PySimpleGUI.OptionMenu(
    fonts, key="Fonts", default_value=fonts[0]), PySimpleGUI.Text("Font size:"), PySimpleGUI.Input(size=(2, 5), key="FontSize", default_text="15")]]
layout = [buttons, [PySimpleGUI.Multiline(size=(61, 95), key='TextBox', auto_refresh=True, autoscroll=True, font=(fonts[0], 15))]]
window = PySimpleGUI.Window('PDFy', layout, finalize=True, auto_size_buttons=True, auto_size_text=True, resizable=True, element_justification='c')

window['Fonts'].TKStringVar.trace("w", callbackOptionMenu)  # type: ignore
window['FontSize'].TKStringVar.trace("w", callbackInput)  # type: ignore
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
            savePDF(values, values["Fonts"], int(values["FontSize"]), fontDir)
        if event == "Fonts":
            changeFont(window, values)
            window["TextBox"].update(size=(80, 150))
        if event == "FontSize":
            changeFontSize(window, values)
    except Exception as e:
        print(e)

window.close()
