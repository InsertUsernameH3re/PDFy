import os
array = []
def findFonts(fontDir):
    for font in os.listdir(fontDir):
        if font.endswith(".ttf"):
            array.append(font)
    return array
