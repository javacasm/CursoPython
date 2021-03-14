import pandas
import matplotlib.pyplot as plt

def recargaDatos(fichero,separador,inicial=0):
    datos = pandas.read_csv(fichero, sep = separador)
    for data in datos:
         print(data)
    x=datos['N']
    y=datos['pi_value']
    if inicial != 0:
        x=x[inicial:]
        y=y[inicial:]
    plt.plot(x,y)
    plt.show()


recargaDatos('evo_orig_pi.csv','\t',inicial=50)
