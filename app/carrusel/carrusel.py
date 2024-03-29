from flask import Blueprint, request, jsonify, render_template
from ..vocal_a_numero import sustituirVocales as enumerar
from ..espaciado import espaciar_cadena as espaciar

carrusel_bp = Blueprint('carrusel', __name__)

@carrusel_bp.route('/carruselNormal')
def carruselIndex():
    return render_template('carruselNormal.html')

def carrusel(palabra):
    resultado = []
    for palabra in palabra.split():
        resultado.append(''.join([palabra[i:] + palabra[:i] + '\n' for i in range(len(palabra))]) + palabra)
    return '```\n' + '\n\n'.join(resultado) + '```'


@carrusel_bp.route('/carruselConvertir', methods=['POST'])
def carruselConvertir():
    palabra = request.json.get('palabra')
    enumera = request.json.get('enumerar')
    espaciado = request.json.get('espaciar')
    mayus = request.json.get('mayusculas')
    minus = request.json.get('minusculas')
    sinFormato = request.json.get('sinformato')
    # metodo = request.form.get('metodo')
    resultado = carrusel(palabra)
    if enumera: 
        resultado = enumerar(resultado)
    if espaciado:
        resultado = espaciar(resultado)
    if mayus:
        resultado = resultado.upper
    if minus:
        resultado = resultado.lower
    if sinFormato:
        pass
        
    print(resultado)
    return jsonify({'resultado': resultado})

