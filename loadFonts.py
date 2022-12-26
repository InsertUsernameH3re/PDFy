import pyglet
fonts = ["Bandal", "Bangwool", "DejaVu Sans", "DejaVu Sans Mono", "DejaVu Serif", "Eunjin", "Eunjin Nakseo", "Firefly Sung", "Gargi", "Garuda", "Guseul", "Kinnari", "Loma", "Mukti Narrow", "Norasi", "Purisa", "Sawasdee", "Tlwg Mono", "Tlwg Typewriter", "Tlwg Typist", "Tlwg Typo", "Umpush", "Waree"]
def loadFonts(fontsAddName, fontDir):
    for font in fontsAddName:
        pyglet.font.add_file(fontDir + font)
    for font in fonts:
        if pyglet.font.have_font(font):
            pyglet.font.load(font)
        else:
            fonts.remove(font)
    return fonts
