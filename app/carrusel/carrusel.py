from flask import Blueprint, request, jsonify, render_template

carrusel_bp = Blueprint('carrusel', __name__)

@carrusel_bp.route('/carruselNormal')
def carruselIndex():
    return render_template('carruselNormal.html')

def carrusel(palabra):
    return '```' + ''.join([palabra[i:] + palabra[:i] + '\n' for i in range(len(palabra))]) + palabra + '```'


@carrusel_bp.route('/carruselConvertir', methods=['POST'])
def carruselConvertir():
    palabra = request.json.get('palabra')
    # metodo = request.form.get('metodo')
    resultado = carrusel(palabra)
    print(resultado)
    return jsonify({'resultado': resultado})

