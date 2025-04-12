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

with connection.cursor() as cursor:
    sql = f"SELECT * FROM {TABLE}"
    cursor.execute(sql)
    # cursor.mogrify # Retorna a string exata que seria enviada ao banco de dados ao chamar o método
    data = cursor.fetchall()
    # print(data)

    for row in data:
        print(row)
    # (1, 'NoteBooks', 'Inovation NoteBooks, last generation of tecnology', Decimal('100.5000'))
    # (2, 'NoteBooks', 'Inovation NoteBooks, last generation of tecnology', Decimal('100.5000'))
    # (3, 'Cell', 'Samsung', Decimal('50.0000'))
    # (4, 'Cell', 'Samsung', Decimal('50.0000'))
