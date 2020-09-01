import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
dataset=pd.read_csv("50_Startups.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values
#manejo de datos categoricos(var-dummy) sin usar labelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([("one_hot_encoder",OneHotEncoder(categories="auto"),[3])],
                     remainder="passthrough"
                     )
x=np.array(ct.fit_transform(x),dtype=np.float)
#eliminamos la primera var dummy
x=x[:,1:]
#divicion set de entrenamiento y testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
#ajustar elmodelo con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(x_train,y_train)
#Prediccion en los datos de testing 
y_pred=regression.predict(x_test)

