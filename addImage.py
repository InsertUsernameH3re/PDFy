from tkinter import INSERT, filedialog
from PIL import Image, ImageTk
filetypesIMG = (('JPG', '*.jpg'), ('PNG', '.png'))
def addImage(window):   
    text = window['Textbox'].widget
    global image
    img = filedialog.askopenfilename(title="Add Image", initialdir="/", filetypes=filetypesIMG, defaultextension=".png")
    img = Image.open(img)
    window["Textbox"].update("//image//")
    image = ImageTk.PhotoImage(img)
    position = text.index(INSERT)
    text.image_create(position, image=image)
