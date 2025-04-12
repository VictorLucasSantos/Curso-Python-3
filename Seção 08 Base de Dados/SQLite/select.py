import sqlite3

from aula205 import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for id, name, wheight in cursor.fetchall():
    print(f'{id} - {name} - {wheight}')
    
cursor.close()
connection.close()