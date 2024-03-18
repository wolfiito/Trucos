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
    enumerate = request.json.get('enumerar')
    espaciado = request.json.get('espaciar')
    # metodo = request.form.get('metodo')
    resultado = carrusel(palabra)
    if enumerate: 
        resultado = enumerar(resultado)
    elif espaciado:
        resultado = espaciar(resultado)
        
    print(resultado)
    return jsonify({'resultado': resultado})

