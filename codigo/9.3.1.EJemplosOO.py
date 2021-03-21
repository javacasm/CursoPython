
class Animal():
    def __init__(self,nombre,numeroPatas):
        self.nombre = nombre
        self.numeroPatas = numeroPatas
        
    def habla(self):
        return ''
    
    def __str__(self):
        return f'me llamo {animal.nombre} tengo {animal.numeroPatas} patas y sueno asi: {animal.habla()}'
        

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 4)
        
    def habla(self):
        return 'Miau'
    
    def __str__(self):
        return 'Soy un gato y' + super().__str__()

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 4)
        
    def habla(self):
        return 'Guau'
    
    def __str__(self):
        return 'Soy un perro y' + super().__str__()


gatoFelipe = Gato('felipe')
perroToby = Perro('Toby')
gusanoMax = Animal('Max', 0)

# Podemos guardar los objetos en cualquiera de las colecciones
animales = [ gatoFelipe, perroToby, gusanoMax]


for animal in animales:
    print(animal)

