from flask import Blueprint, request, jsonify, render_template
from ..vocal_a_numero import sustituirVocales as enumerar
from ..espaciado import espaciar_cadena as espaciar

deletreoC_bp = Blueprint('deletreoC', __name__)

@deletreoC_bp.route('/deletreoC')
def deletreoEnC():
    return render_template('deletreoC.html')

def deletrear(palabra):
    resultado = []
    deletreoC = []
    for palabra in palabra.split():
        deletreoC.append(palabra)
        for i in range(1, len(palabra) - 1):
            deletreoC.append(palabra[i])
        deletreoC.append(palabra[::-1])
        resultado.append('\n'.join(deletreoC))
        deletreoC = []
    return '```\n' + '\n\n'.join(resultado) + '```'  # Invertimos toda la palabra



@deletreoC_bp.route('/hacerDeletreoC', methods=['POST'])
def deletreoC():
    palabra = request.json.get('palabra')
    enumera = request.json.get('enumerar')
    espaciado = request.json.get('espaciar')
    mayus = request.json.get('mayusculas')
    minus = request.json.get('minusculas')
    sinFormato = request.json.get('sinformato')
    # metodo = request.form.get('metodo')
    resultado = deletrear(palabra)
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
