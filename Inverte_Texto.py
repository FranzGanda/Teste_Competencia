def inverte (texto):
    if len(texto) == 1:
        return texto
    elif len(texto) > 1:
        return inverte(texto[1:]) + texto[0]

print(inverte(texto = input()))
