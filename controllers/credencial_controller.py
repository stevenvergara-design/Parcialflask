from flask import Blueprint, render_template, request, redirect, session

from models.credencial_model import crear_credencial, obtener_credenciales
from utils.security import encrypt_password, decrypt_password

credencial = Blueprint("credencial", __name__)


def login_required():
    if "user" not in session:
        return redirect("/login")


@credencial.route("/crear", methods=["GET", "POST"])
def crear():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        servicio = request.form["servicio"]
        usuario = request.form["usuario"]
        password = request.form["password"]

        encrypted = encrypt_password(password)

        crear_credencial(servicio, usuario, encrypted)
        return redirect("/dashboard")

    return render_template("crear.html")


@credencial.route("/ver")
def ver():
    if "user" not in session:
        return redirect("/login")

    datos = obtener_credenciales()
    datos_descifrados = []

    for d in datos:
        password = decrypt_password(d[3])
        datos_descifrados.append((d[0], d[1], d[2], password))

    return render_template("ver.html", datos=datos_descifrados)