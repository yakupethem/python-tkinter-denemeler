from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def sec():
    # print(combo.get())
    sonuc = Label(text=combo.get()).place(x=10, y=50, width=100)
    sonuc1 = Label(text=c1.get()).place(x=100, y=100, width=100)
    sonuc2 = Label(text="radio seçimi" + str(r.get())).place(x=130, y=50, width=100)

def tikla():
    messagebox.showinfo("mesaj","mesaj gönderildi")


pencere = Tk()

pencere.title("yakocan40")
pencere.geometry("500x300+700+200")
"""
yazi = Label(text="ilk başlık",font="Verdana 22 bold")
yazi.pack(side="left")  # top, left, right, bottom
yazi2 = Label(text="ikinci başlık",font="Verdana 22 bold")
yazi2.pack(side="left")
yazi3 = Label(text="üçüncü başlık",font="Verdana 22 bold")
yazi3.pack(fill="x")  # x, y
yazi4 = Label(text="dördüncü başlık",font="Verdana 22 bold")
yazi4.pack(expand="no")  # yes, no
# pack() komponentleri paketliyor
# grid() arayüzü parçalara bölüyor kare kare
# place() x,y koordinatlarıyla yerletiiriyor

yazi5 = Label(text="ilk başlık", font="Verdana 22 bold")
yazi5.grid(row=1, column=5)
yazi6 = Label(text="ikinci başlık", font="Verdana 22 bold")
yazi6.grid(row=5, column=5)

yazi7 = Label(text="ilk başlık", font="Verdana 22 bold")
yazi7.place(x=150, y=50)
yazi8 = Label(text="ikinci başlık", font="Verdana 22 bold")
yazi8.place(x=30, y=90)
"""

combo = Combobox()
combo["values"] = ("bir şehir seçin", "istanbul", "ankara", "bursa", "eskişehir", "kırşehir")
combo.current(0)
combo.place(x=10, y=10)

buton = Button(text="seç", command=lambda: sec()).place(x=160, y=8)
c1 = StringVar()
cb = Checkbutton(text="seç tuşu", variable=c1, onvalue="seçili", offvalue="seçili değil", command=sec).place(x=20,
                                                                                                             y=100)
r = IntVar()
rb = Radiobutton(text="radyo tuşu", variable=r, value=1, command=sec).place(x=200, y=100)
rb2 = Radiobutton(text="radyo tuşu2", variable=r, value=2, command=sec).place(x=200, y=130)

mesaj=Button(text="gönder",command=tikla).place(x=200,y=200)
#messagebox.showinfo("bilgi","bilgi içeriği")
#messagebox.showerror("hata mesajı","yanlış yaptınız")
#messagebox.showwarning("dikat","bir hata var")
#messagebox.askyesno("yol ayrımı","devam mı?")

pencere.mainloop()
