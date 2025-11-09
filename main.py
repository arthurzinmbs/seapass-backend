import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="seapass",
        user="postgres",    # seu usuário do PostgreSQL
        password="1234"   # sua senha do PostgreSQL
    )
    print("Conexão com o banco realizada com sucesso!")
except Exception as e:
    print("Erro ao conectar ao banco:", e)
