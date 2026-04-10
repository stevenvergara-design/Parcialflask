from models.db import get_connection

def crear_usuario(password_hash):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuario (password_hash)
        VALUES (?)
    """, (password_hash,))

    conn.commit()
    conn.close()


def obtener_usuario():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM usuario LIMIT 1")
    user = cursor.fetchone()

    conn.close()
    return user