#!/usr/bin/env python
# coding: utf-8

# # Tareas 6
# 
# License CC by sa 
# by @javacasm
# 
# ## [Ejercicios pyNative](pyNative)
# 
# ## [Gráfica COVID-19](covid19)
# 
# ## [Gráficos de xkcd](https://www.google.com/search?q=xkcd+chart&client=ubuntu&hs=jv9&sxsrf=ALeKk02VC8dWKQL1l28bjOwb1PHO47w4hA:1588004710057&tbm=isch&source=iu&ictx=1&fir=P6kcHtl0K1bQlM%253A%252CzdXFuI_O3X9b3M%252C_&vet=1&usg=AI4_-kQtvcG_2P09M-PtSV6rwI1JNhCHng&sa=X&ved=2ahUKEwiJzZPFgonpAhWGHhQKHZIaDzEQ9QEwDHoECAoQNA#imgrc=rokBOGaNJ57voM)

# ## Ejercicios pyNative <a id="pyNative"></a>
# 
# Ejercicios de [esta web](https://pynative.com/python-matplotlib-exercise/)

# In[14]:


import matplotlib.pyplot as plt


# In[115]:


# Documentación sobre Pandas https://colab.research.google.com/github/ageron/handson-ml2/blob/master/tools_pandas.ipynb
import pandas 

datos = pandas.read_csv('data/company_sales_data.csv',sep = ',') # Es un dataFrame (tabla)

datos


# In[10]:


# Con columnas con nombre (Series)

datos['shampoo']


# In[11]:


# Si iteramos un DataFrame vemos los nombres
for data in datos:
    print(data)


# In[12]:


# Si iteramos una Serie vemos los valores

for data in datos['toothpaste']:
    print(data)


# ## Exercise 1: Read "Total profit" of all months and show it using a line plot
# Total profit data provided for each month. Generated line plot must include the following properties: –
# 
# X label name = Month Number
# Y label name = Total profit

# In[33]:


yValues = datos['total_profit']
xValues = datos['month_number']

plt.plot(xValues,yValues)
plt.title('Beneficio total mensual')
plt.xticks(xValues)
plt.yticks([100000,200000,300000,400000,500000])
plt.xlabel('Mes')
plt.ylabel('Beneficio total')


# ## Exercise Question 2: Get Total profit of all months and show line plot with the following Style properties
# 
# Generated line plot must include following Style properties: –
# 
# Line Style dotted and Line-color should be red
# Show legend at the lower right location.
# X label name = Month Number
# Y label name = Sold units number
# Add a circle marker.
# Line marker color as read
# Line width should be 3

# In[34]:


yValues = datos['total_profit']
xValues = datos['month_number']

plt.plot(xValues,yValues,'ro--',label='Beneficio total')
# plt.plot(monthList, profitList, label = 'Profit data of last year',color='r', marker='o', markerfacecolor='k',linestyle='--', linewidth=3)
plt.title('Beneficio total mensual')
plt.xticks(xValues)
plt.yticks([100000,200000,300000,400000,500000])
plt.xlabel('Mes')
plt.ylabel('Beneficio total')
plt.legend(loc='lower right')


# ## Exercise Question 3: Read all product sales data and show it  using a multiline plot
# Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).

# In[46]:


xColumnName ='month_number'

xValues = datos[xColumnName]

yColumnNames = []
for columnName in datos:
    if columnName != xColumnName and not 'total' in columnName:
        yColumnNames.append(columnName)

for yColumnName in yColumnNames:
    plt.plot(datos[xColumnName],datos[yColumnName],label = yColumnName)

plt.title('Ventas mensuales')
plt.xticks(xValues)
#plt.yticks([100000,200000,300000,400000,500000])
plt.xlabel('Mes')
plt.ylabel('Ventas mensuales')
plt.legend(loc='best')


# ## Exercise Question 4: Read toothpaste sales data of each month and show it using a scatter plot
# 
# Also, add a grid in the plot. gridline style should “–“.

# yValues = datos['toothpaste']
# xValues = datos['month_number']
# 
# plt.scatter(xValues,yValues,50,label='Pasta de dientes')
# plt.xlabel('Mes')
# plt.ylabel('Pastas de dientes vendidas')
# plt.title('Ventas mensuales de pasta de dientes')
# plt.legend(loc = 'upper left')

# ## Exercise Question 5: Read face cream and facewash product sales data and show it using the bar chart
# 
# The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.

# In[70]:


xValues = datos['month_number']
faceCream = datos['facecream']
faceWash = datos['facewash']

anchoBarra = 0.25

plt.bar([barra1 - anchoBarra/2 for barra1 in xValues],faceCream,width = anchoBarra, label = 'Crema de la cara')
plt.bar([barra2  + anchoBarra/2 for barra2 in xValues],faceWash,width = anchoBarra, label = 'Jabón de la cara')
plt.title('Ventas de productos para la cara')
plt.xlabel('Mes')
plt.ylabel('Ventas de productos')
plt.legend(loc='upper left')
plt.grid(True, linewidth= 1, linestyle="--")


# ## Exercise Question 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
# 

# In[73]:


xValues = datos['month_number']
bathingsoap = datos['bathingsoap']

plt.bar(xValues,bathingsoap, label = 'Jabón de baño')
plt.title('Ventas de jabon de baño')
plt.xlabel('Mes')
plt.ylabel('Ventas de producto')
plt.legend(loc='upper left')
plt.grid(True, linewidth= 1, linestyle="--")

plt.savefig('VentasJabon.png',transparent = True, dpi=150)


# ## Exercise Question 7: Read the total profit of each month and show it using the histogram to see most common profit ranges

# In[75]:


yValues = datos['total_profit']
xValues = datos['month_number']

plt.plot(xValues,yValues)


# In[ ]:


numCajas = 5
minValue = min(yValues)
maxValue = max(yValues)
paso = (maxValue - minValue)//numCajas
cajas = range(minValue,maxValue,paso)

plt.hist(yValues,cajas)


# ## Exercise Question 8: Calculate total sale data for last year for each product and show it using a Pie chart
# 
# In Pie chart display Number of units sold per year for each product in percentage.

# In[92]:


xColumnName ='month_number'

productNames = []
sumProducts = []
for columnName in datos:
    if columnName != xColumnName and not 'total' in columnName:
        productNames.append(columnName)
        sumProducts.append(datos[columnName].sum())


plt.pie(sumProducts, labels=productNames,autopct='%1.1f%%')
plt.title('Ventas mensuales')
plt.legend(loc='best')


# ## Exercise Question 9: Read Bathing soap facewash of all months and display it using the Subplot

# In[109]:


xValues = datos['month_number']
bathingsoap = datos['bathingsoap']
faceWash = datos['facewash']

plt.subplot(2,1,1)
plt.plot(xValues,bathingsoap,'rx-')
plt.title('Gel de baño')

plt.xticks([])
plt.subplot(2,1,2)
plt.plot(xValues,faceWash,'go--')
plt.title('Jabón para la cara')
plt.xticks(xValues)
plt.xlabel('Mes')
plt.ylabel('Ventas en unidades')


# In[103]:


# The pro way
xValues = datos['month_number']
bathingsoap = datos['bathingsoap']
faceWash = datos['facewash']

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(xValues, bathingsoap, label = 'Gel de baño', color='k', marker='o', linewidth=3)
axarr[0].set_title('Gel de baño')
axarr[1].plot(xValues, faceWash, label = 'Jabón para la cara', color='r', marker='o', linewidth=3)
axarr[1].set_title('Jabón para la cara')


# ## Exercise Question 10: Read all product sales data and show it using the stack plot

# In[114]:


xValues = datos['month_number']
faceCremSalesData   = datos ['facecream']
faceWashSalesData   = datos ['facewash']
toothPasteSalesData = datos ['toothpaste']
bathingsoapSalesData   = datos ['bathingsoap']
shampooSalesData   = datos ['shampoo']
moisturizerSalesData = datos ['moisturizer']

plt.plot([],[],color='m', label='Crema de la cara', linewidth=5)
plt.plot([],[],color='c', label='Jabón  de la cara', linewidth=5)
plt.plot([],[],color='r', label='Pasta de dientes', linewidth=5)
plt.plot([],[],color='k', label='Jabón de baño', linewidth=5)
plt.plot([],[],color='g', label='Champú', linewidth=5)
plt.plot([],[],color='y', label='Acondionador', linewidth=5)

plt.stackplot(xValues, faceCremSalesData, faceWashSalesData, toothPasteSalesData, 
              bathingsoapSalesData, shampooSalesData, moisturizerSalesData, 
              colors=['m','c','r','k','g','y'])

plt.xlabel('Mes')
plt.ylabel('Ventas en unidades')
plt.title('todos los productos acumulados')
plt.legend(loc='upper left')
plt.show()


# ## Gráfica COVID-19 <a id="covid19"></a>
# 
# Se trata de reproducir [el estudio de Joos Korstanje](https://towardsdatascience.com/modeling-logistic-growth-1367dc971de2) sobre la evolución de COVID-19 y el ajuste a una ecuación logística aplicándolo a los [datos de España](https://github.com/datadista/datasets/tree/master/COVID%2019) (datos de datadista), por ejemplo a los de [evolución de los casos en las distintas comunidades autónomas](https://github.com/datadista/datasets/blob/master/COVID%2019/ccaa_covid19_casos.csv)
# 
# Se puede seguir todo el cálculo en su [jupyter notebook](https://jooskorstanje.com/modeling-logistic-growth-corona.html)
# 
