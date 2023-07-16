import sys
sys.path.append(r'.\models')



from flask import Flask, render_template, request
from aula import Aula
from lista_de_aulas import ListaDeAulas

app = Flask(__name__)

@app.route("/")
def home():
  aulas = ListaDeAulas()
  return render_template("home.html", aulas=aulas)

@app.route("/add_aula", methods=["GET", "POST"])
def add_aula():
  if request.method == "GET":
    return render_template("add_aula.html")
  else:
    nome = request.form["nome"]
    carga_horaria = request.form["carga_horaria"]
    aulas_semana = request.form["aulas_semana"]
    aula = Aula(nome, carga_horaria, aulas_semana)
    aula.adicionar_aula(aula)
    return redirect(url_for("home"))

@app.route("/add_falta", methods=["GET", "POST"])
def add_falta():
  if request.method == "GET":
    return render_template("add_falta.html")
  else:
    nome = request.form["nome"]
    aula = aula.buscar_aula(nome)
    aula.adicionar_falta()
    return redirect(url_for("home"))

@app.route("/show_aulas", methods=["GET"])
def show_aulas():
  aulas = ListaDeAulas()
  return render_template("show_aulas.html", aulas=aulas)

if __name__ == "__main__":
  app.run(debug=True)