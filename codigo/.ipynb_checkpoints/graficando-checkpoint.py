"""
Gráficos con matplotlib
Documentación oficial de matplotlib
https://colab.research.google.com/github/ageron/handson-ml2/blob/master/tools_matplotlib.ipynb#scrollTo=st_zTGp_aeJQ
"""

import matplotlib.pyplot as plt

# series
lista = [10,2,15,56]
plt.plot(lista)
plt.show() # No es necesario ponerlo en jupyter pero si cuando trabajamos en otros entornos. Tras esta llamada se renderiza todo"

# x vs y

serieX = [1,4,6,7]
serieY = [2,4,5,7]
plt.plot(serieX,serieY)

# axis([minX,maxX,minY,maxY])
plt.axis([0,10,0,8])

# dibujando funciones

import numpy as np
# 50 puntos equiespaciados entre el mínimo y el máximo y lo guarda en un array de numpy
x = np.linspace(-2,2,50) 

y = x**2 

plt.plot(x, y)

# poniéndolo bonito

plt.title('Square function')
plt.xlabel('x')
plt.ylabel('y = x**2')
plt.grid(True)

# Podemos añadir varios gráficos

z = y + 2
plt.plot(x,y)
plt.plot(x,z)
# o añadiendo todas los pares de valores en una llamada

plt.plot(x,y,x,z)
# Usando distintos tipos de linea http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
w = z - 5

plt.plot(x,y,'r')
plt.plot(x,z,'g--')
plt.plot(x,w,'b.')

plt.plot(x,y,'r^')
plt.plot(x,z,'g:')
plt.plot(x,w,'bx')

# Cuando la tengamos a nuestro gusto la podemos guardar como fichero

plt.savefig('my_square_function.png', transparent=True)
# Scater (punto x,y sueltos)
x = [2, 4, 5, 7, 6]
y = [6, 3, 4, 6, 9]

plt.scatter(x,y,0.5,c='Black')
#help(plt.scatter)

x = np.linspace(-1.5, 1.5, 30)
px = 0.8
py = px**2

plt.plot(x, x**2, px, py, 'ro')

bbox_props = dict(boxstyle='rarrow,pad=0.3', ec='b', lw=2, fc='lightblue')
plt.text(px-0.2, py, 'Beautiful point', bbox=bbox_props, ha='right')

bbox_props = dict(boxstyle='round4,pad=1,rounding_size=0.2', ec='black', fc='#EEEEFF', lw=5)
plt.text(0, 1.5, 'Square function\n$y = x^2$', fontsize=20, color='black', ha='center', bbox=bbox_props)

plt.show()



# O usando el aspecto de los graficos de xkcd
# instalamos font humor-sans con sudo apt install fonts-humor-sans 
with plt.xkcd():
    plt.plot(x, x**2, px, py, 'ro')

    bbox_props = dict(boxstyle='rarrow,pad=0.3', ec='b', lw=2, fc='lightblue')
    plt.text(px-0.2, py, 'Beautiful point', bbox=bbox_props, ha='right')

    bbox_props = dict(boxstyle='round4,pad=1,rounding_size=0.2', ec='black', fc='#EEEEFF', lw=5)
    plt.text(0, 1.5, 'Square function\n$y = x^2$', fontsize=20, color='black', ha='center', bbox=bbox_props)

    plt.show()
# Referencias
"""
Sobre scatter con grupos de distintos colores https://pythonspot.com/matplotlib-scatterplot/


[Make beautifull plots in jupyter](https://towardsdatascience.com/making-plots-in-jupyter-notebook-beautiful-more-meaningful-23c8a35c0d5d)

[Histogramas](https://www.tutorialspoint.com/numpy/numpy_histogram_using_matplotlib.htm)

[Matplotlib in jupyter](https://medium.com/@1522933668924/using-matplotlib-in-jupyter-notebooks-comparing-methods-and-some-tips-python-c38e85b40ba1)
"""
   