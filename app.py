from flask import Flask, render_template, request, redirect, session
from database import obtener_tareas, agregar_tarea, completar_tarea, eliminar_tarea
import os

app = Flask(__name__, static_folder='static')
app.secret_key = "1dda2d7e60f8def051e265fa045d3d917a1fdc9bae4225b8ca0e6530b56a1ddb"

@app.route("/")
def index():
    usuario = session.get("usuario")
    if not usuario:
        return redirect("/login")
    tareas = obtener_tareas(usuario["id"])
    return render_template("index.html", tareas=tareas, usuario=usuario)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/callback")
def callback():
    # Supabase maneja el callback via JavaScript
    return render_template("callback.html")

@app.route("/guardar-sesion", methods=["POST"])
def guardar_sesion():
    data = request.json
    session["usuario"] = {
        "id": data["id"],
        "email": data["email"],
        "nombre": data.get("nombre", data["email"])
    }
    return {"ok": True}

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/agregar", methods=["POST"])
def agregar():
    usuario = session.get("usuario")
    if not usuario:
        return redirect("/login")
    titulo = request.form.get("titulo")
    if titulo:
        agregar_tarea(titulo, usuario["id"])
    return redirect("/")

@app.route("/completar/<int:id>")
def completar(id):
    if not session.get("usuario"):
        return redirect("/login")
    completar_tarea(id)
    return redirect("/")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    if not session.get("usuario"):
        return redirect("/login")
    eliminar_tarea(id)
    return redirect("/")

if __name__ == "__main__":
    app.run()