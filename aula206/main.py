"""
Base de dados com MySQL e pymysql
Criando tabela com conexão com pymysql
"""

import os
import pymysql
import dotenv

# Carrega as variaveis de ambiente .env
dotenv.load_dotenv()

TABLE = "customers"

# Criando a conexão
connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    port=int(os.environ["MYSQL_PORT"]),
    charset="utf8mb4",
)

print(os.environ["MYSQL_HOST"])
print(os.environ["MYSQL_USER"])
print(os.environ["MYSQL_PASSWORD"])
print(os.environ["MYSQL_DATABASE"])

# utilizando a conexão e utilizando um cursor da conexão
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE} ("
            "                                       id INT NOT NULL AUTO_INCREMENT"
            "                                      , name VARCHAR(50) NOT NULL"
            "                                      , age INT NOT NULL"
            "                                      , PRIMARY KEY (id)"
            "                                      )"
        )
    # Realizar commit para registrar alterações realizadas na conexão local para global
    connection.commit()
    with connection.cursor() as cursor:
        numero_de_linhas_afetadas = cursor.execute(
            f"INSERT INTO {TABLE}" "(name, age) VALUES ('Victor', 22)"
        )
    print(numero_de_linhas_afetadas)
    connection.commit()
