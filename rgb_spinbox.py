from tkinter import *
from tkinter.ttk import *


def renk():
    k = kirmiziSpin.get()
    m = maviSpin.get()
    y = yesilSpin.get()
    kh = hex(int(k))
    mh = hex(int(m))
    yh = hex(int(y))
    color = "#" + kh.replace("0x", "") + mh.replace("0x", "") + yh.replace("0x", "")
    print(color)
    print(kh)
    pencere.configure(bg=color)


pencere = Tk()

pencere.title("yakocan40")
pencere.geometry("500x300+700+200")

kirmiziLabel = Label(text="kırmızı")
kirmiziLabel.place(x=20, y=20)
kirmiziSpin = Spinbox(pencere, from_=0, to=15, command=renk)
kirmiziSpin.place(x=60, y=20, width=50)

maviLAbel = Label(text="mavi")
maviLAbel.place(x=20, y=50)
maviSpin = Spinbox(pencere, from_=0, to=15, command=renk)
maviSpin.place(x=60, y=50, width=50)

yesilLabel = Label(text="yesşil")
yesilLabel.place(x=20, y=80)
yesilSpin = Spinbox(pencere, from_=0, to=15, command=renk)
yesilSpin.place(x=60, y=80, width=50)

spin = Spinbox(pencere, values=(3, 8, 11), width=5)
spin.place(x=100, y=150)

var = IntVar()
var.set(36)
spin2 = Spinbox(pencere, from_=0, to=100, width=5, textvariable=var)
spin2.place(x=170, y=150)

pencere.mainloop()
