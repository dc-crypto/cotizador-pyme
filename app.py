from flask import Flask, render_template, request, redirect
from database import obtener_tareas, agregar_tarea, completar_tarea, eliminar_tarea

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    tareas = obtener_tareas()
    return render_template("index.html", tareas=tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form.get("titulo")
    if titulo:
        agregar_tarea(titulo)
    return redirect("/")

@app.route("/completar/<int:id>")
def completar(id):
    completar_tarea(id)
    return redirect("/")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    eliminar_tarea(id)
    return redirect("/")

if __name__ == "__main__":
    app.run()