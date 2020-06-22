from tkinter import *

pencere = Tk()
pencere.geometry("500x500")

lred = Frame(bg="red", width=100, height=100)
lred.place(x=20, y=20)
bred = Button(lred, text="kımızının butonu")
bred.place(x=0, y=0)

lblue = Frame(bg="BLUE", width=100, height=100)
lblue.place(x=150, y=150)
bblue = Button(lblue, text="mavinin butonu")
bblue.place(x=0, y=0)

lframe = LabelFrame(text="label başlığı",width=200,height=100,bg="yellow")
lframe.place(x=200, y=20)
blf=Button(lframe,text="etiketlinin butonu")
blf.place(x=0,y=10)

mainloop()
