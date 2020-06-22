from tkinter import *

pencere=Tk()

mb=Menubutton(text="salatalar",relief=RAISED)
mb.place(x=30,y=30)

mbMenu=Menu(mb,tearoff=0)
mb.config(menu=mbMenu)
coban=IntVar()
mevsim=IntVar()
a=IntVar
b=IntVar
mbMenu.add_checkbutton(label="çoban salata",variable=coban)
mbMenu.add_checkbutton(label="mevsim salata",variable=mevsim)

mb2=Menubutton(text="çorbalar",relief=RAISED)
mb2.place(x=90,y=30)

mb2Menu=Menu(mb2,tearoff=0)
mb2.config(menu=mb2Menu)

kelle=StringVar()
ayak=StringVar()
mb2Menu.add_checkbutton(label="kelle paça",variable=kelle)
mb2Menu.add_checkbutton(label="ayak paça",variable=ayak)


mainloop()