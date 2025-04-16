import sqlite3
from pathlib import Path

# Obtendo a raiz do projeto
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / 'banco.db'
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'wheight REAL'
    ')'
    )

connection.commit()

# registrar valores nas colunas das tabelas
# execute executa somente um comando e executemany varios
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id ,name, wheight)'
    'VALUES (NULL, "Teste", 10.5), (NULL, "Teste1", 10.0)' 
) 

connection.commit()

# Deleta os dados da tabela
# cursor.execute(
#     f'DELETE TABLE IF NOT EXISTS {TABLE_NAME}'
#     )

# Deleta a sequencia dos indices da tabela
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name = "{TABLE_NAME}"'
    )

# Fazendo a inserção de dados de forma correta para tratar SQLInjection
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (name, wheight)'
    'VALUES (?, ?)',
    ('Teste', 10.5)
) 

# fazendo inserção com dicionario
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (name, wheight)'
    'VALUES (:nome, :peso)',
    {'nome': 'Teste', 'peso': 10.5}
) 

# alteração de registros
cursor.execute(
    f'UPDATE {TABLE_NAME}'
    '    SET name = "Qualquer"'
    '  WHERE id = 2 '
    )

# sempre utilizar o commit por ultimo para poder confirmar as alterações no banco
connection.commit()

cursor.close()
connection.close()