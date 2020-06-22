from tkinter import *
from tkinter import messagebox


from hesap_makinesi_sınıfı import *

pencere = Tk()

pencere.title("yakocan40")
pencere.geometry("500x300+700+200")

sayi1 = Label(text="Sayı1:", bg="grey").place(x=0, y=10)
sayi1_giris = Entry(width=10)
sayi1_giris.place(x=40, y=10)
sayi2 = Label(text="Sayı2:", bg="grey").place(x=110, y=10)
sayi2_giris = Entry(width=10)
sayi2_giris.place(x=150, y=10)

deger1 = sayi1_giris.get()
deger2 = sayi2_giris.get()
#sonuc = Label(text="sonuç", bg="grey", fg="black").place(x=230, y=10, width=50)
#hesap=hesapMakinesi(sayi2_giris.get(),sayi1_giris.get())
tus_topla = Button(text="+", font="20", command=lambda :topla()).place(x=20, y=40)
tus_cikar = Button(text="-", font="20", command=lambda :cikar()).place(x=50, y=40)
tus_carp = Button(text="*", font="20", command=lambda :carp()).place(x=80, y=40)
tus_bol = Button(text="/", font="20", command=lambda :bol()).place(x=110, y=40)

def topla():
    hesap = hesapMakinesi(int(sayi1_giris.get()),int(sayi2_giris.get()))
    sonuc = Label(text=str(hesap.topla()), bg="yellow", fg="red").place(x=230, y=10, width=50)
    #messagebox.showinfo("Sonuç", message=hesap.topla())
def cikar():
    hesap = hesapMakinesi(int(sayi1_giris.get()),int(sayi2_giris.get()))
    sonuc = Label(text=str(hesap.cikart()), bg="yellow", fg="red").place(x=230, y=10, width=50)
def carp():
    hesap = hesapMakinesi(int(sayi1_giris.get()),int(sayi2_giris.get()))
    sonuc = Label(text=str(hesap.carp()), bg="yellow", fg="red").place(x=230, y=10, width=50)
    #messagebox.showinfo("Sonuç", message=hesap.topla())
def bol():
    hesap = hesapMakinesi(int(sayi1_giris.get()),int(sayi2_giris.get()))
    sonuc = Label(text=str(hesap.bol()), bg="yellow", fg="red").place(x=230, y=10, width=50)

pencere.mainloop()
