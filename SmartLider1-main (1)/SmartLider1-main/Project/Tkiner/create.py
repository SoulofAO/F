import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
#cursor.execute("""CREATE TABLE Aplications
         #         (name text, text text, fun1 text,
            #       fun2 text, fun3 text,fun4 text)

albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
c1=["fun1","1"]
c="1"
a=cursor.execute("SELECT * FROM Aplications WHERE ? =?", c1)

print(cursor.fetchall())
