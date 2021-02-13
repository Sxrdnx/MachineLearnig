# -*- coding: utf-8 -*-
"""
Spyder Editor
Regresion polinomida 
"""
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#cargar dataset
dataSet = pd.read_csv("Position_Salaries.csv")
"""
si se usa 
x = dataSet.iloc[:,1] <--- esto es un vector pero para los algoritmos necesitamos que x sea una matriz
por eso se cambia 
pero para -y- no importa
"""
#separamos el data set
x = dataSet.iloc[:,1:2].values
y = dataSet.iloc[:,2].values
#como hay poco informacion no se separa 
#ajustamos el modelo primero la lineal
from sklearn.linear_model import LinearRegression
regressionLineal = LinearRegression()
regressionLineal.fit(x,y)

#ajustamos el modelo de regresion polinomica 
from sklearn.preprocessing import PolynomialFeatures
poli_Regresion = PolynomialFeatures(degree=4) # convierte las varibles independientes de forma polinomial con el parametro del grado 
x_poly = poli_Regresion.fit_transform(x)
regression2 = LinearRegression()
regression2.fit(x_poly, y)

plt.ticklabel_format(useOffset=False, style='plain')
#visualizacion de la regrecion Lineal
plt.scatter(x,y,color="red")
plt.plot(x,regressionLineal.predict(x),color='blue')
plt.title("Modelo lineal") 
plt.xlabel("nivel/posicion enpleado")
plt.ylabel("salario en ($)")
plt.show()

#visualizar el modelo polinomico
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid),1)
plt.scatter(x,y,color="red")
x_poly2=poli_Regresion.fit_transform(x_grid)
plt.plot(x_grid,regression2.predict(x_poly2),color='green')
plt.title("Modelo polinomico") 
plt.xlabel("nivel/posicion enpleado")
plt.ylabel("salario en ($)")
plt.show()

#predicciones segun el modelo 
perdyL = regressionLineal.predict(x)
predyP = regression2.predict(x_poly)





