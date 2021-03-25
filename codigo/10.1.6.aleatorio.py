from random import choice, sample, randint
colores = ('rojo', 'verde', 'azul', 'blanco', 'negro', 'amarillo')


# Elegimos un n´umero aleatorio entre unos extremos
print(colores[randint(0,len(colores)-1)]) # ¡Podria salir 6!

for i in range(5):
    print (choice(colores))
    
print(sample(colores,4))
