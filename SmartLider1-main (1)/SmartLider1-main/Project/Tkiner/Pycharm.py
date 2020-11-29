import sqlite3
conn = sqlite3.connect('orders.db')
import tkinter as tk

print(A1)
def ide1():
   btn.configure(bg="red")
   A1=1
def ide2():
   btn.configure(bg="red")
def ide3():
   btn.configure(bg="red")
window = tk.Tk()
window.title("Смена Названий")
window.geometry('800x300')
btn = tk.Button(window, text="Функция1", command=ide1())
btn.grid(column=1, row=1)
btn1 = tk.Button(window, text="Функция2", command=ide2())
btn1.grid(column=1, row=2)
btn1 = tk.Button(window, text="Функция2", command=ide3())
btn1.grid(column=1, row=3)