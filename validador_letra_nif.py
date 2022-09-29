def calcularLetra(dni):
    resultado = dni % 23
    if resultado == 0:
        letra = "T"
    elif resultado == 1:
        letra = "R"
    elif resultado == 2:
        letra = "W"
    elif resultado == 3:
        letra = "A"
    elif resultado == 4:
        letra = "G"
    elif resultado == 5:
        letra = "M"
    elif resultado == 6:
        letra = "Y"
    elif resultado == 7:
        letra = "F"
    elif resultado == 8:
        letra = "P"
    elif resultado == 9:
        letra = "D"
    elif resultado == 10:
        letra = "X"
    elif resultado == 11:
        letra = "B"
    elif resultado == 12:
        letra = "N"
    elif resultado == 13:
        letra = "J"
    elif resultado == 14:
        letra = "Z"
    elif resultado == 15:
        letra = "S"
    elif resultado == 16:
        letra = "Q"
    elif resultado == 17:
        letra = "V"
    elif resultado == 18:
        letra = "H"
    elif resultado == 19:
        letra = "L"
    elif resultado == 20:
        letra = "C"
    elif resultado == 21:
        letra = "K"
    else:
        letra = "E"
    return letra