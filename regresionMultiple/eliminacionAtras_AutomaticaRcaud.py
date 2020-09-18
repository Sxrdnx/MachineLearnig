#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:47:23 2020

@author: sxrdnx
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

dataSet=pd.read_csv("50_Startups.csv")
x=dataSet.iloc[:,:-1].values
y=dataSet.iloc[:,4].values
#datos categoricos 
ct=ColumnTransformer([('one_hot_encoder',OneHotEncoder(categories='auto'),[3])],
                     remainder= "passthrough"
    ) 
x=np.array(ct.fit_transform(x),dtype=np.float)
x=x[:,1:]   
def backwardElimination(x,sl):
    numVars= len (x[0]) 
    temp=np.zeros((50,6)).astype(int)
    mark=50
    for i in range(0,numVars):
        regressor_OLS=sm.OLS(y,x.tolist()).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        adjR_before = regressor_OLS.rsquared_adj.astype(float)        
        mark-=1
        if maxVar > sl:
            for j in range (0,numVars-i):
                if (regressor_OLS.pvalues[j].astype(float)==maxVar):
                    temp[:,j]=x[:,j]
                    x=np.delete(x,j,1)
                    tmp_regressor = sm.OLS(y, x.tolist()).fit()                    
                    adjR_after = tmp_regressor.rsquared_adj.astype(float) 
                    if(adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))                        
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary()) 
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()                        
    return x

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)  
regression=LinearRegression()
regression.fit(x_train,y_train)
x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis =1)#columna para el coeficiente de relacion en la variable dependiente
SL=0.05
x_op=x[:,[0,1,2,3,4,5]]
x_Model=backwardElimination(x_op, SL)
                                