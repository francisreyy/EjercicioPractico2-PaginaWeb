import os
from flask import Flask, render_template, request, redirect, url_for, flash

from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'csyduped@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'csyduped@gmail.com'
mail = Mail(app)

@app.route("/")
def index():
    info_evento = {
        1: { "nombre": "Rally MTB 2025",
        "organizador": "Club Social y Deportivo Unidos por el Deporte",
        "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km …",
        "fecha": "24 de Octubre de 2025",
        "horario": "8am",
        "lugar": "Tandil, Buenos Aires",
        "tipo_carrera": "MTB rural",
        "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "100"},
                            2: {"nombre": "Larga" ,"valor": "200"}},
        "Auspiciantes": ["ausp1","auspN"]
        }
    }

    title = "Club Social y Deportivo Unidos por el Deporte"
    return render_template('index.html',page_title = title, info = info_evento)

@app.route("/registration")
def registration():
    title = "Registro"
    return render_template('registration.html',page_title = title)

if __name__ == "__main__":
    app.run("localhost", port="5000", debug=True)