from flask import Blueprint, render_template, request, redirect, session
import bcrypt

from models.usuario_model import crear_usuario, obtener_usuario

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        password = request.form["password"]

        hashed = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        crear_usuario(hashed)
        return redirect("/login")

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form["password"]
        user = obtener_usuario()

        if user and bcrypt.checkpw(password.encode("utf-8"), user[0]):
            session["user"] = "admin"
            return redirect("/dashboard")

        return "Contraseña incorrecta"

    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/login")