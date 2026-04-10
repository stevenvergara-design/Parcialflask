from models.db import get_connection

def crear_credencial(servicio, usuario, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO credenciales (servicio, usuario, password_encriptada)
        VALUES (?, ?, ?)
    """, (servicio, usuario, password))

    conn.commit()
    conn.close()


def obtener_credenciales():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM credenciales")
    datos = cursor.fetchall()

    conn.close()
    return datos