def espaciar_cadena(cadena_a_espaciar):
    palabra = ' '.join(c for c in cadena_a_espaciar if c != ' ')
    palabra.strip()
    return palabra