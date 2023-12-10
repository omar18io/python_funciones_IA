from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
@app.route("/crear-tabla")
def crear_tabla():
    conn = sqlite3.connect("usuario.db")
    c = conn.cursor()
    c.execute("""
              CREATE TABLE usuarios (username text, password text)
              """)
    c.execute("INSERT INTO usuarios VALUES ('omar', '!codefxRoma')")
    c.execute("INSERT INTO usuarios VALUES ('rosas', '!tdgr53')")
    c.execute("INSERT INTO usuarios VALUES ('rojarib', '!tokdg56')")
    conn.commit()
    conn.close()
    return "Base de datos creada"
@app.route("/login")
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM usuarios WHERE username = '{username}' AND password = '{password}'")
    result = c.fetchall()
    conn.close()
    if not result:
        return "Credenciales Inválidas", 401
    columns = ["username", "password"]
    result_dict = [dict(zip(columns, row)) for row in result]
    return jsonify(result_dict)
if __name__ == "__main__":
    app.run(debug=True)







