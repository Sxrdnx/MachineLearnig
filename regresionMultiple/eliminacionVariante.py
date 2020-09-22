import numpy as np
import pandas as pd
dataSet=pd.read_csv("50_Startups.csv")
x=dataSet.iloc[:,:-1].values
y=dataSet.iloc[:,4].values
#Datos categoricos
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer ([("one_hot_encoder",OneHotEncoder(categories="auto"),[3])],remainder="passthrough")
x=np.array(ct.fit_transform(x),dtype=np.float)
#eliminamos para evitar colinealidad
x=x[:,1:]
#divicion en entrenamiento y testeo
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
#ajustar el modelo de regression lineal multiple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(x_train,y_train)
#predeccion de los resultados con el conjunto de testing
y_pred=regression.predict(x_test)
#construccion del modelo optimo de RLM utilizando eliminacion hacia atras 
import statsmodels.api as sm
x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)
sl=0.05
x_opt=x[:,[0,1,2,3,4,5]]
regression_OLS=sm.OLS(endog=y,exog=x_opt.tolist()).fit()
print(regression_OLS.summary())


