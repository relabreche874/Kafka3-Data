import sqlite3

conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()
cursor.execute('Select * from transaction1')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
