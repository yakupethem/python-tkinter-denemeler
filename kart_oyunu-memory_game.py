from random import random
from tkinter import *
import time
from tkinter import messagebox

pencere = Tk()
pencere.title("kart oyunu")
pencere.geometry("400x400+400+150")

ikonlar = ["!", "N", ",", "k", "b", "v", "w", "z"]
ikonlar = ikonlar * 2
kartlar = []
rasgele_kartlar = []
ikon_kart_sirasi = 0
oyuncu_tiklama_sayisi = 0
ilk_acilan_ikon_kart_sirasi = -1  # henüz bir button tıklamnmamış anlamında -1 verdik
acilan_ikili_kart_sayisi = 0

for satir in range(4):
    for sutun in range(4):
        cerceve = LabelFrame(width=100, height=100)
        cerceve.grid(row=satir, column=sutun)
        cerceve.rowconfigure(satir, weight=1)
        cerceve.columnconfigure(sutun, weight=1)
        cerceve.grid_propagate(False)
        index = int(random() * len(ikonlar))
        kart = Button(cerceve, text="", font="Webdings 50",
                      width=20, height=7, command=lambda s=ikon_kart_sirasi: kart_dondur(s))
        kart.grid(row=satir, column=sutun)
        kartlar.append(kart)
        rasgele_kartlar.append(ikonlar[index])
        ikon_kart_sirasi += 1
        ikonlar.pop(index)


def kart_dondur(kart_sirasi):
    global oyuncu_tiklama_sayisi, ilk_acilan_ikon_kart_sirasi, acilan_ikili_kart_sayisi
    oyuncu_tiklama_sayisi += 1
    kartlar[kart_sirasi].config(text=rasgele_kartlar[kart_sirasi], state="disable")

    if ilk_acilan_ikon_kart_sirasi == -1:
        ilk_acilan_ikon_kart_sirasi = kart_sirasi
    else:
        if rasgele_kartlar[ilk_acilan_ikon_kart_sirasi] == rasgele_kartlar[kart_sirasi]:
            acilan_ikili_kart_sayisi += 1
            if acilan_ikili_kart_sayisi == len(rasgele_kartlar) // 2:
                messagebox.showinfo("bilgi", str(oyuncu_tiklama_sayisi) + " kere tıklayarak oyunu bitirdiniz")
        else:
            kartlar[kart_sirasi].after(10, lambda: kartlari_Geri_dondur(kart_sirasi, ilk_acilan_ikon_kart_sirasi))
            ilk_acilan_ikon_kart_sirasi = -1
    ilk_acilan_ikon_kart_sirasi = -1


def kartlari_Geri_dondur(kart_sirasi, ilk_acilan_ikon_kart_sirasi):
    kartlar[kart_sirasi].config(text="", state="active")
    kartlar[ilk_acilan_ikon_kart_sirasi].config(text="", state="active")
    time.sleep(2)


mainloop()
