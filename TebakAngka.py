import tkinter as tk
from tkinter import Button, ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Games Tebak Angka')
root.geometry('300x300+200+150')
root.resizable(False, False)

# functions for result/hint


# functions for 'angka'
def btn1_clicked():
    angka = 1

def btn2_clicked():
    angka = 2

def btn3_clicked():
    angka = 3

def btn4_clicked():
    angka = 4

def btn5_clicked():
    angka = 5

def btn6_clicked():
    angka = 6

def btn7_clicked():
    angka = 7

def btn8_clicked():
    angka = 8

def btn9_clicked():
    angka = 9

def btn5_clicked():
    angka = 5



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
btn1 = ttk.Button(root, text="1", command=btn1_clicked)
btn1.grid(column=0, row=2, padx=5, pady=5)

btn2 = ttk.Button(root, text="2", command=btn2_clicked)
btn2.grid(column=1, row=2, padx=5, pady=5)

btn3 = ttk.Button(root, text="3", command=btn3_clicked)
btn3.grid(column=2, row=2, padx=5, pady=5)

btn4 = ttk.Button(root, text="4", command=btn4_clicked)
btn4.grid(column=0, row=3, padx=5, pady=5)

btn5 = ttk.Button(root, text="5", command=btn5_clicked)
btn5.grid(column=1, row=3, padx=5, pady=5)

btn6 = ttk.Button(root, text="6", command=btn6_clicked)
btn6.grid(column=2, row=3, padx=5, pady=5)

btn7 = ttk.Button(root, text="7", command=btn7_clicked)
btn7.grid(column=0, row=4, padx=5, pady=5)

btn8 = ttk.Button(root, text="8", command=btn8_clicked)
btn8.grid(column=1, row=4, padx=5, pady=5)

btn9 = ttk.Button(root, text="9", command=btn9_clicked)
btn9.grid(column=2, row=4, padx=5, pady=5)

root.mainloop()