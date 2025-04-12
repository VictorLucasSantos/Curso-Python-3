"""
Base de dados com MySQL e pymysql
Realizando inserção no banco com pymsql e utilizando dicionário
"""

import os
import pymysql
import dotenv

# Carrega as variaveis de ambiente .env
dotenv.load_dotenv()

TABLE = "products"

# Criando a conexão
connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    port=int(os.environ["MYSQL_PORT"]),
    charset="utf8mb4",
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE} ("
            "                                       id INT NOT NULL AUTO_INCREMENT"
            "                                      , name VARCHAR(50) NOT NULL"
            "                                      , description  TEXT"
            "                                      , price DECIMAL(16, 4) NOT NULL "
            "                                      , PRIMARY KEY (id)"
            "                                      )"
        )
    connection.commit()
    with connection.cursor() as cursor:
        data = {"name": "Cell", "description": "Samsung", "price": 50.0}
        # REALIZANDO INSERÇÃO COM DICIONÁRIO
        numero_de_linhas_afetadas = cursor.execute(
            f"INSERT INTO {TABLE}"
            "(name, description, price) VALUES (%(name)s, %(description)s, %(price)s)",
            data,
        )
    print(numero_de_linhas_afetadas)
    connection.commit()
    with connection.cursor() as cursor:
        data = {
            {"name": "Cell", "description": "Samsung", "price": 50.0},
            {"name": "Tablet", "description": "Nokia", "price": 200.0},
            {"name": "Computer", "description": "Dell", "price": 500.0},
        }
        # REALIZANDO INSERÇÃO COM DICIONÁRIO DE DICIONÁRIOS COM VÁRIOS VALORES
        numero_de_linhas_afetadas = cursor.executemany(
            f"INSERT INTO {TABLE}"
            "(name, description, price) VALUES (%(name)s, %(description)s, %(price)s)",
            data,
        )
    print(numero_de_linhas_afetadas)
    connection.commit()
