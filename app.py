# app.py
from flask import Flask, request, render_template
from calc import Disciplina, Aula, ListaDeAulas, Historico, Acao

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('attendance_form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    nome = request.form['nome']
    carga_horaria = int(request.form['carga_horaria'])
    aulas_semana = int(request.form['aulas_semana'])
    faltas = int(request.form['faltas'])

    disciplina = Disciplina(nome, carga_horaria, aulas_semana)
    for _ in range(faltas):
        disciplina.adicionar_falta()

    return f'Você faltou {disciplina.mostrar_faltas()} aulas na disciplina {disciplina.nome}.'

if __name__ == '__main__':
    app.run(debug=True)
