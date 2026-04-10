from flask import Flask, render_template, redirect, session
import sqlite3

from controllers.auth_controller import auth
from controllers.credencial_controller import credencial
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.register_blueprint(auth)
app.register_blueprint(credencial)

DB = "database.db"


def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password_hash BLOB NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS credenciales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        servicio TEXT,
        usuario TEXT,
        password_encriptada TEXT
    )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuario")
    user = cursor.fetchone()

    conn.close()

    if user:
        return redirect("/login")
    else:
        return redirect("/register")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


if __name__ == "__main__":
    init_db()
    app.run()