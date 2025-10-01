from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)



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