import sqlite3
conn = sqlite3.connect('orders.db')
import tkinter as tk


class Factor():
    def __init__(self,number_factor,text,id,column,row):
       self.number_factor=number_factor
       self.text = text
       self.bg_color=""
       self.Activ=0
       self.id=id
       self.column=column
       self.row=row
       self.a=tk.Button(window, text=self.text, command=self.clicked)

    def clicked(self):
        if self.Activ==0:
           self.bg_color="red"
           self.Activ=1
           print(1)
           self.a.configure(bg="red")
        else:
            self.bg_color = "white"
            self.Activ = 0
            self.a.configure(bg="blue")
            print(0)


    def draw(self,column,row,color):
        self.a.grid(column=column,row=row)
def Finder():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    t1=[]
    cursor.execute("SELECT * FROM Aplications")
    row = cursor.fetchone()
    return row

z=Finder()

def Find(z,t):
    a1=[]
    for x in t:
        a1.append(str(x.Activ))
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aplications WHERE (fun1=? AND fun2=? AND fun3=? AND fun4=?)", a1)
    row = cursor.fetchone()
    print(row)
    sum=0
    for x in row:
        sum=sum+1
    return ([row],[sum-2])




class Aplications():
    def __init__(self,a,t2):
        self.name=a[0]
        self.text=a[1]
        self.counter=t2
        self.row=0
        self.id=t2
    def Print(self):
        lbl = tk.Label(window, text=self.name)
        lbl.grid(column=self.counter, row=self.counter)





def Restart1():
    t=[]
    for x in range(4):
      a=Factor(x,b[x],x,1,x)
      a.draw(column=1,row=x,color="blue")
      t.append(a)
    return t


def clicked0():
      y = Find(1, t)
      print(y[1])
      global A
      A=(y)
      x=Restart2()


def Restart2():
  d=A[0]
  t1=[]
  t2=0
  for x in d:
      t2=t2+1
      z=Aplications(x,t2)
      z.Print()
      t1.append(x)
  return t1

window = tk.Tk()
window.title("Поиск программ")
window.geometry('800x300')

btn = tk.Button(window, text="Поиск", command=clicked0)
btn.grid(column=3, row=1)
a=0
b=["Функция1","Функция2","Функция3","Функция4"]
t=Restart1()
clicked0()
t1=Restart2()

#y1=y[1]
#y1=int(y1)



txt = tk.Entry(window,width=30)
txt.grid(column=5, row=5)

window.mainloop()
