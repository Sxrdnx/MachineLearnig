#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:29:02 2020

@author: sxrdnx
"""
#esta elminacion hacia atras es con solo p-valores
import statsmodels.api as sm
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
dataSet=pd.read_csv("50_Startups.csv")
x=dataSet.iloc[:,:-1].values
y=dataSet.iloc[:,4].values
#Datos categoricos
ct=ColumnTransformer([('one_hot_encoder',OneHotEncoder(categories="auto"),[3])],
                     remainder="passthrough"
                     )
x=np.array(ct.fit_transform(x),dtype=np.float)
#eliminacion de la primera variable dummy
x=x[:,1:]
#divicion en train y test 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)  

def backwardElimination(x,sl):
    numVars= len (x[0])
    for i in range(0,numVars):
        regressor_OLS=sm.OLS(y,x.tolist()).fit()
        maxVar=max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0,numVars-i):
                if(regressor_OLS.pvalues[j].astype(float)==maxVar):
                    x=np.delete(x,j,1)                  
    regressor_OLS.summary()                 
    return x

regression=LinearRegression()
regression.fit(x_train,y_train)
x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis =1)#columna para el coeficiente de relacion en la variable dependiente
SL=0.05
x_op=x[:,[0,1,2,3,4,5]]
x_Model=backwardElimination(x_op, SL)
    
                    
                    
                    
                
        