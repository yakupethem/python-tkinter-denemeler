import time
from tkinter import *

pencere = Tk()
pencere.title("geri sayaç")
pencere.geometry("300x300")

i=10
def geri():
            global i
            i-=1
            l.configure(text=str(i),fg="red",font="Verdana 33 bold")
            pencere.after(1000,geri)
            if i ==-1 :

                l.configure(text="son", fg="red", font="Verdana 33 bold")
            elif i ==-2:
                quit(geri())
                pencere.after(3000, geri)
def cıkıs():
    exit(geri())
l = Label()
l.place(x=125, y=100)
b = Button(text="başla", command=geri)
b.place(x=125, y=150)
c = Button(text="çıkış", command=cıkıs)
c.place(x=125, y=250)
mainloop()
