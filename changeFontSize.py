from changeFont import changeFont

def changeFontSize(window, values):
    try:
        size = int(values["FontSize"])
        if size > 99 or size < 1:
            window["FontSize"].update(value="15")
            changeFont(window, values)
        else:
            changeFont(window, values)
    except:
        window["FontSize"].update(value="15")
        changeFont(window, values)
