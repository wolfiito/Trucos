from flask import Blueprint, request, jsonify, render_template
from ..vocal_a_numero import sustituirVocales as enumerar
from ..espaciado import espaciar_cadena as espaciar

crucePalabras_bp = Blueprint('crucePalabras', __name__)

@crucePalabras_bp.route('/crucePalabras')
def crucePalabrasTemplates():
    return render_template('crucePalabras.html')

@crucePalabras_bp.route('/cruce_palabras', methods=['POST'])
def crucePalabras():
    palabra = request.json.get('palabra')
    enumera = request.json.get('enumerar')
    espaciado = request.json.get('espaciar')
    mayus = request.json.get('mayusculas')
    minus = request.json.get('minusculas')
    sinFormato = request.json.get('sinformato')
    resultado = []
    for palabra in palabra.split():
        resultado.append(palabra)
        longitud = len(palabra)
        for i in range(1, longitud):
            resultado.append(palabra[i] * i + palabra[i:])
    resultado = '```\n' + '\n'.join(resultado) + '```'
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

    return jsonify({ 'resultado': resultado })