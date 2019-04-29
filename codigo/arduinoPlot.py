# -*- coding: utf-8 -*-
import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit

values = []

plt.ion()
cnt=0
#Se define el puerto serie y la velocidad de transmisión
serialArduino = serial.Serial('/dev/ttyUSB0', 9600)
#Se define la funcion plotValues
def plotValues():
    plt.title('Valor recibido por el puerto Serie')
    plt.grid(True)
    plt.ylabel('Valores')
    plt.plot(values, 'rx-', label='valores')
    plt.legend(loc='upper right')
#Se define la función para cerrar el puerto serie
def doAtExit():
    serialArduino.close()
    print("Close serial")
    print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

atexit.register(doAtExit)
#Se escribe en pantalla que el puerto serie de Arduino esta abierto
print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

#Se realiza una precarga de un valor de prueba
for i in range(0,26):
    values.append(0)

while True:
    while (serialArduino.inWaiting()==0):
        pass
    print("readline()")
    valueRead = serialArduino.readline(500)

    #Comprueba si se transmite o no un valor correcto
    try:
        valueInInt = int(valueRead)
        print(valueInInt)
        if valueInInt <= 1024:
            if valueInInt >= 0:
                values.append(valueInInt)
                values.pop(0)
                drawnow(plotValues)
            else:
                print("Invalido: numero negativo")
        else:
            print("Invalido:demasiado grande")
    except ValueError:
        print("Invalido: No se puede transmitir")
