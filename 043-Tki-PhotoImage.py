#!/usr/bin/env python

from base64  import *
# http://effbot.org/tkinterbook/photoimage.htm
# https://www.base64encode.org/
obrazok = """
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
AAAASUVORK5CYII=
"""

from Tkinter import *
#from PIL import Image, ImageTk

okno = Tk()

photo = PhotoImage(file="Untitled.gif")
#photo = PhotoImage(file="lenna.pgm")
#bin_obrazok = b64decode(obrazok)
#photo = PhotoImage(data=bin_obrazok)


# PIL - ine ako gif/pgm
#image = Image.open("lenna.jpg")
#photo = ImageTk.PhotoImage(image)



label = Label(okno,image=photo)
label.image = photo # keep a reference!
label.pack()

mainloop()

