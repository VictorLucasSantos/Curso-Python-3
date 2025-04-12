"""
Base de dados com MySQL e pymysql
Criando tabela com conexão com pymysql
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

print(os.environ["MYSQL_HOST"])
print(os.environ["MYSQL_USER"])
print(os.environ["MYSQL_PASSWORD"])
print(os.environ["MYSQL_DATABASE"])

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
    # Utilizando a conexão e utilizando um cursor da conexão (OUTRA FORMA DE REALIZAR INSERÇÕES COM CONEXÕES DE BANCO DE DADOS COM PYTHON)
    with connection.cursor() as cursor:
        # REALIZANDO INSERÇÃO COM TUPLA PARA PODER REALIZAR INSERÇÃO COM A MELHOR FORMA DE PREVENIR SQL INJECTION
        numero_de_linhas_afetadas = cursor.execute(
            f"INSERT INTO {TABLE}" "(name, description, price) VALUES (%s, %s, %s)",
            ("NoteBooks", "Inovation NoteBooks, last generation of tecnology", 100.50),
        )
    print(numero_de_linhas_afetadas)
    connection.commit()
"""
Ao usar placeholders (%s) e passar os valores como uma tupla,
o pymysql (e outros drivers compatíveis com o PEP 249)
trata os valores como parâmetros e os escapa corretamente, prevenindo SQL Injection.
Ou seja, o método utilizado realmente é uma das melhores práticas para prevenir SQL Injection.
No entanto, dizer que é a "melhor forma" pode ser subjetivo,
pois prepared statements no nível do banco de dados podem ser ainda mais eficientes.
"""
