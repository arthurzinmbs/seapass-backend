from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

# Conexão com o banco
try:
    conn = psycopg2.connect(
        host="localhost",
        database="seapass",
        user="postgres",
        password="1234"
    )
    print("Conexão com o banco realizada com sucesso!")
except Exception as e:
    print("Erro ao conectar ao banco:", e)

# Criação do Flask app
app = Flask(__name__)
CORS(app)  # Permite requisições de qualquer origem

# Teste de saúde da API
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "API funcionando!"})

# Cadastro de usuário
@app.route("/api/cadastro", methods=["POST"])
def cadastro():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    telefone = data.get("telefone")
    data_nascimento = data.get("data_nascimento")
    senha = data.get("senha")

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email, telefone, data_nascimento, senha) VALUES (%s, %s, %s, %s, %s)",
            (nome, email, telefone, data_nascimento, senha)
        )
        conn.commit()
        cursor.close()
        return jsonify({"success": True, "message": "Cadastro realizado com sucesso!"})
    except Exception as e:
        return jsonify({"success": False, "erro": str(e)})

# Rodar o servidor
if __name__ == "__main__":
    app.run(debug=True, port=4000)
