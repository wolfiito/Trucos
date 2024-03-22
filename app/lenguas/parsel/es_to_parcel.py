from flask import Blueprint, request, jsonify, render_template
from ...vocal_a_numero import sustituirVocales as enumerar
from ...espaciado import espaciar_cadena as espaciar

esParcel_bp = Blueprint('esp_to_parcel', __name__)

@esParcel_bp.route('/esToParcelTemplate')
def esToParcelTemplate():
    return render_template('es_to_parcel.html')

@esParcel_bp.route('/esp_to_parcel', methods=['POST'])
def esToParcel():
    traduccion = {
        'a': 'esh',  'b': 'ch',  'c': 'eish', 'd': 'shi', 'e': 'ash',
        'f': 'asha', 'g': 'ei',  'h': 'shis',  'i': 'osh', 'j': 'xim',
        'k': 'ss',   'l': 'suh', 'm': 'xan',  'n': 'sh',  'o': 'ush',
        'p': 'cah',  'q': 'xii', 'r': 'in',   's': 'shs',  't': 'cass',
        'u': 'ish',  'v': 'aus', 'w': 'xi',   'x': 'shh', 'y': 'sss',
        'z': 'xiy',  'á': 'esh', 'é': 'ash',  'í': 'osh', 'ó': 'ush',
        'ú': 'ish',  'ü': 'ish', ' ': ' '
    }
    palabra = request.json.get('palabra')
    enumera = request.json.get('enumerar')
    espaciado = request.json.get('espaciar')
    
    if espaciado:
        palabra = espaciar(palabra)
    
    texto_traducido = ''
    
    for letra in palabra.lower():
        if letra in traduccion:
            texto_traducido += traduccion[letra]
        else:
            texto_traducido += letra
    
    if enumera:
        texto_traducido = enumerar(texto_traducido)
    print(texto_traducido)
    return jsonify({ 'resultado': texto_traducido })