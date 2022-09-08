from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import Button, ttk
from tkinter.messagebox import showinfo
import random
from turtle import onclick

root = tk.Tk()
root.title('Games Tebak Angka')
root.geometry('300x300+200+150')
root.resizable(False, False)

# variables
hint_rendah = "tebakanmu terlalu rendah"
hint_tinggi = "tebakanmu terlalu tinggi"

# functions for result/hint
angka = random.randint(1, 9)
kesempatan = 0

def angka_random(text):

    global hint_rendah, hint_tinggi, kesempatan

    tebakan = text

    while kesempatan < 5:
        try:
            tebakan = text
        except ValueError: tebakan = 9999
        kesempatan += 1
        if tebakan < angka:
            label_hint.config(text = hint_rendah)
        elif tebakan > angka:
            label_hint.config(text=hint_tinggi)
        elif tebakan == angka: break

    if tebakan == angka:
        label_res.config(text= "Kamu menebaknya dalam " + str(kesempatan) + " percobaan!")
    else:
        label_res.config(text= "\033[1mKamu gagal, angka yang benar adalah " + str(angka))


def onclick(text):
    angka_random(text)

# configure the grid
root.columnconfigure(0, weight=3)
root.columnconfigure(0, weight=3)
root.columnconfigure(2, weight=2)
root.columnconfigure(3, weight=2)
root.columnconfigure(4, weight=2)
root.columnconfigure(5, weight=3)
root.columnconfigure(6, weight=3)

# Title
label_title = ttk.Label(
    root,
    text='Games Tebak Angka',
    font=("Helvetica", 14))

label_title.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5, columnspan=4)

# Instruction label
label_ins = ttk.Label(
    root,
    text='Pilih angka yang ingin ditebak! \nAnda memiliki 5 kesempatan untuk menebak.',
    font=("Helvetica", 10))

label_ins.grid(column=0, row=1, sticky=tk.NW, padx=5, pady=15, columnspan=4)

# Hint label
label_hint = ttk.Label(
    root,
    text='Hint: ',
    font=("Helvetica", 10))

label_hint.grid(column=0, row=5, sticky=tk.NW, padx=5, pady=10, columnspan=4)

# Result label
label_res = ttk.Label(
    root,
    text='Tebakan Anda Benar!',
    font=("Helvetica", 10))

label_res.grid(column=0, row=6, sticky=tk.NW, padx=5, pady=15, columnspan=4)

# button
btn1 = ttk.Button(root, text="1", command=lambda:onclick(1))
btn1.grid(column=0, row=2, padx=5, pady=5)

btn2 = ttk.Button(root, text="2", command=lambda:onclick(2))
btn2.grid(column=1, row=2, padx=5, pady=5)

btn3 = ttk.Button(root, text="3", command=lambda:onclick(3))
btn3.grid(column=2, row=2, padx=5, pady=5)

btn4 = ttk.Button(root, text="4", command=lambda:onclick(4))
btn4.grid(column=0, row=3, padx=5, pady=5)

btn5 = ttk.Button(root, text="5", command=lambda:onclick(5))
btn5.grid(column=1, row=3, padx=5, pady=5)

btn6 = ttk.Button(root, text="6", command=lambda:onclick(6))
btn6.grid(column=2, row=3, padx=5, pady=5)

btn7 = ttk.Button(root, text="7", command=lambda:onclick(7))
btn7.grid(column=0, row=4, padx=5, pady=5)

btn8 = ttk.Button(root, text="8", command=lambda:onclick(8))
btn8.grid(column=1, row=4, padx=5, pady=5)

btn9 = ttk.Button(root, text="9", command=lambda:onclick(9))
btn9.grid(column=2, row=4, padx=5, pady=5)

root.mainloop()