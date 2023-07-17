
from flask import Flask
from config import MODELS_DIR
from routes import main as main_blueprint
from aula import Aula
from lista_de_aulas import ListaDeAulas
from db import init_db

app = Flask(__name__)
app.register_blueprint(main_blueprint)

def init_database():
    init_db

if __name__ == "__main__":
    # init_db()
    app.run(debug=True)
