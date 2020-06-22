from tkinter import *
from random import *


def karistir():
    b = []
    for i in range(1, 10):
        b.append(Button(text=str(i), font="15", width=2, command=lambda x=i: yaz(x)))
    sayac = 0
    for i in range(3):
        for j in range(3):
            shuffle(b)
            b[sayac].place(x=20 + 50 * j, y=50 + 50 * i)
            sayac += 1

def yaz(x):
    s = len(giris.get())
    giris.insert(s, str(x))


hesap = 5
s1 = 0


def islemler(x):
    global hesap
    hesap = x
    global s1
    s1 = float(giris.get())
    giris.delete(0, "end")


s2 = 0


def hesapla():
    global s2
    s2 = float(giris.get())
    global hesap
    sonuc = 0
    if (hesap == 0):
        sonuc = s1 + s2
    elif (hesap == 1):
        sonuc = s1 - s2
    elif (hesap == 2):
        sonuc = s1 * s2
    elif (hesap == 3):
        sonuc = s1 / s2
    giris.delete(0, 'end')
    giris.insert(0, str(sonuc))


pencere = Tk()
pencere.geometry("250x300")

giris = Entry(font="16", width=20, justify=RIGHT)
giris.place(x=20, y=20)
b = []
for i in range(1, 10):
    b.append(Button(text=str(i), font="15", width=2, command=lambda x=i: yaz(x)))
sayac = 0
for i in range(3):
    for j in range(3):
        b[sayac].place(x=20 + 50 * j, y=50 + 50 * i)
        sayac += 1

islem = []
for i in range(4):
    islem.append(Button(font=15, width=2, command=lambda x=i: islemler(x)))
islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"

for i in range(4):
    islem[i].place(x=170, y=50 + 50 * i)

eb = Button(text="=", font=20, width=2, bg="red", command=hesapla)
eb.place(x=120, y=200)
sb = Button(text="0", font=15, width=2, command=lambda x=0: yaz(x))
sb.place(x=20, y=200)
nb = Button(text=".", font=15, width=2, command=lambda x=".": yaz(x))
nb.place(x=70, y=200)




karB = Button(text="karıştır", font=15, width=20,bg="yellow", command=lambda : karistir())
karB.place(x=20, y=250)


mainloop()
