from tkinter import *
from tkinter.scrolledtext import ScrolledText


def sec():
    #lb3.insert(END,list[m])
    print(m)

pencere = Tk()
pencere.geometry("400x400")
list=["php","java","python","c++"]
lb = Listbox(selectmode=BROWSE)
lb3 = Listbox(selectmode=BROWSE)
lb2 = ScrolledText(width=10, height=10)
lb2.place(x=200, y=10)
for i in range(len(list)):
    lb.insert(i,list[i])
m=lb.curselection
lb.place(x=10, y=10)
b = Button(text="seç", command=sec)
b.place(x=140, y=50)


mainloop()
