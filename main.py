from flask import Flask, render_template
from app.carrusel.carrusel import carrusel_bp
from app.deletreo.C import deletreoC_bp
from app.lenguas.parsel.es_to_parcel import esParcel_bp
from app.cruce.cruce_palabras import crucePalabras_bp 

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('inicio.html')

app.register_blueprint(carrusel_bp)
app.register_blueprint(deletreoC_bp)
app.register_blueprint(esParcel_bp)
app.register_blueprint(crucePalabras_bp)

if __name__ == '__main__':
    app.run(debug=True)