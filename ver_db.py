import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM credenciales")
datos = cursor.fetchall()

for d in datos:
    print(d)

conn.close()