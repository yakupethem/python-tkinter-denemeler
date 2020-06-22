from tkinter import *


def buyukluk(deger):
    yazi.configure(font="Helvetica "+deger)  #yazı tipinden sonra bir boşluk bırak


pencere = Tk()


slider = Scale(from_=2, to=20, orient=HORIZONTAL, command=buyukluk)
slider.place(x=10, y=10)

yazi = Label(text="yazı fontu")
yazi.place(x=80, y=80)

mainloop()
