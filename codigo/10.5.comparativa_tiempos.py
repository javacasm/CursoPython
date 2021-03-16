# vamos a hacer una comparativa de tiempos
import pandas
import matplotlib.pyplot as plt

datos_c = pandas.read_csv('codigo/data/tiempos_c.csv',sep=' ')
datos_cO4 = pandas.read_csv('codigo/data/tiempos_cO4.csv',sep=' ')
datos_pypy = pandas.read_csv('codigo/data/tiempos_pypy.csv',sep=' ')
datos_python = pandas.read_csv('codigo/data/tiempos_python.csv',sep=' ')

#datos_c.plot(x='N',y='T')
#datos_cO4.plot(x='N',y='T') 
# Unir series con concat https://www.kite.com/python/answers/how-to-merge-two-pandas-series-into-a-dataframe-in-python#
plt.plot(datos_c['N'],datos_c['T'],label = 'C')
plt.plot(datos_cO4['N'],datos_cO4['T'],label = 'C -O4')
plt.plot(datos_pypy['N'],datos_pypy['T'],label = 'pypy')
plt.plot(datos_python['N'],datos_python['T'],label = 'Python')
plt.legend()
plt.ylabel('Tiempo (s)')
plt.xlabel('N cifras de Pi')
plt.yscale('log')
plt.title('Tiempo para calcular N cifras de Pi')
plt.show()
