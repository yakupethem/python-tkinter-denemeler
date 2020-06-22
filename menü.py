from tkinter import *

def fonk():
    pencere2=Tk()
    lab=Label(pencere2,text="çalıştı")
    lab.place(x=50,y=50)
    mainloop()

pencere=Tk()
pencere.geometry("500x500")

menucubugu=Menu(pencere)

dosya=Menu(menucubugu,tearoff=0)
dosya.add_command(label="yeni",command=fonk)
dosya.add_command(label="aç",command=fonk)
dosya.add_command(label="kaydet",command=fonk)
dosya.add_separator()
dosya.add_command(label="çıkış",command=fonk)
menucubugu.add_cascade(label="dosya",menu=dosya)
#pencere.config(menu=menucubugu)

duzen=Menu(menucubugu,tearoff=0)
duzen.add_command(label="kes",command=fonk)
duzen.add_command(label="kopyala",command=fonk)
duzen.add_command(label="yabıştır",command=fonk)
menucubugu.add_cascade(label="düzen",menu=duzen)
pencere.config(menu=menucubugu)





mainloop()