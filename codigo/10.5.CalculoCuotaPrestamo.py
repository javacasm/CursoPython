

def calculoCuota(capital, interesPercent,plazo):
    interes = interesPercent/100
    interesMensual = interes/12
    plazoMeses = plazo * 12
    rN = pow(1+interesMensual,-plazoMeses)
    cuota = capital/((1-rN)/interesMensual)
    return cuota


def getCuotaFromDatos():
    capital =  float(input('Importe del Prestamo?: '))
    interesPercent = float(input('Tipo de interes anual?: '))
    plazo = int(input('Plazo en años?: '))
    return calculoCuota(capital, interesPercent, plazo)


def getPagos(capital, cuota, interesMensual):
    capitalRestante = capital
    print('Deuda\tCuota\tIntereses\tReduccion de capital')
    while capitalRestante>0:
        intereses = capitalRestante*interesMensual
        reduccionCapital = cuota - intereses
        print(f'{capitalRestante:5.2f}\t{cuota:5.2f}\t{intereses:5.2f}\t{reduccionCapital:5.2f}')
        capitalRestante -= cuota
        

cuota = calculoCuota(115000,2,25)
print(f'{cuota:5.2f}')
getPagos(115000,cuota,2/1200)
