from flask import Blueprint, render_template, request, redirect, url_for
from config import MODELS_DIR
from aula import Aula
from lista_de_aulas import ListaDeAulas
from db import get_db

main = Blueprint('main', __name__)

@main.route("/")
def home():
    db = get_db()
    aulas_db = db.execute('SELECT * FROM aulas').fetchall()
    return render_template("home.html", aulas=aulas_db)

@main.route("/add_aula", methods=["GET", "POST"])
def add_aula():
    if request.method == "GET":
        return render_template("add_aula.html")
    else:
        nome = request.form["nome"]
        carga_horaria = int(request.form["carga_horaria"])
        aulas_semana = int(request.form["aulas_semana"])
        aula = Aula(nome, carga_horaria, aulas_semana)
        db = get_db()
        db.execute(
            'INSERT INTO aulas (nome, carga_horaria, aulas_semana, semanas, total_aulas, aulas_faltadas) VALUES (?, ?, ?, ?, ?, ?)',
            (aula.nome, aula.carga_horaria, aula.aulas_semana, aula.semanas, aula.total_aulas, aula.aulas_faltadas)
        )
        db.commit()
        return redirect(url_for("main.home"))

@main.route("/add_falta", methods=["GET", "POST"])
def add_falta():
    lista_de_aulas = ListaDeAulas()
    if request.method == "GET":
        nome = request.args.get('nome', default = None, type = str)
        if nome is not None:
            aula = lista_de_aulas.buscar_aula(nome)
            if aula is not None:
                faltas = aula[5]
                faltas_restantes = (aula[4] * 0.25) - aula[5]
            else:
                faltas = 0
                faltas_restantes = 0
        else:
            faltas = 0
            faltas_restantes = 0
        aulas = lista_de_aulas.get_all_aulas()
        return render_template("add_falta.html", aulas=aulas, selected_nome=nome, faltas=faltas, faltas_restantes=faltas_restantes)
    else:
        nome = request.form["nome"]
        aula = lista_de_aulas.buscar_aula(nome)
        aula.adicionar_falta()
        return redirect(url_for("main.home"))



@main.route("/show_aulas", methods=["GET"])
def show_aulas():
    db = get_db()
    aulas_db = db.execute('SELECT * FROM aulas').fetchall()
    return render_template("show_aulas.html", aulas=aulas_db)
