from tkinter import *
from random import *

liste = ["yellow", "red", "orange", "blue"]
#rastegele = randint(0, len(liste))


def fonk():
    rastegele = randint(0, len(liste))
    t2 = Toplevel(bg=liste[rastegele-1])


pencere = Tk()

# t=Toplevel(bg="red")

b = Button(text="pencere oluştur", command=fonk)
b.place(x=10, y=10)


mainloop()
