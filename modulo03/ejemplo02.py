def clasificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Cero"

assert clasificar_numero(5) == "Positivo", "La clasificación no es correcta."
assert clasificar_numero(-3) == "Negativo", "La clasificación no es correcta."
assert clasificar_numero(0) == "Cero", "La clasificación no es correcta."