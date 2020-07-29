import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import pandas as pd
#carga del csv
dataset=pd.read_csv("Salary_Data.csv")#cambiar de notacion cientifica punto flotante=%0.f
#Divicion de variables dependiente e intependientes
x=dataset.iloc[:,0].values
y=dataset.iloc[:,1].values
#divicion test y entrenamiento
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)
#regrecion lineal
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
x_train=x_train.reshape(-1,1)
regression.fit(x_train,y_train)
x_test=x_test.reshape(-1,1)
#prediccion del conjunto de test
y_pred=regression.predict(x_test)
#visualizar resultados de entrenamiento 
plt.scatter(x_train,y_train,color="red")
plt.plot(x_train,regression.predict(x_train),color="blue")
plt.title("Sueldo VS Años de Experiencia (conjunto de entrenamiento)")
plt.xlabel("Años de experiencia")
plt.ylabel("Sueldo en($)")
plt.show()
#visualizacion resultados de test
plt.scatter(x_test,y_test,color="red")
plt.plot(x_train,regression.predict(x_train),color="blue")
plt.title("Sueldo VS Años de Experiencia (conjunto de testing)")
plt.xlabel("Años de experiencia")
plt.ylabel("Sueldo en($)")
plt.show()


