#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:12:55 2020

@author: sxrdnx
"""
import numpy as np
from sklearn.impute import SimpleImputer
import pandas as pd
#carga del csv
dataset=pd.read_csv("Data.csv")#cambiar de notacion cientifica punto flotante=%0.f
#Divicion de variables dependiente e intependientes
x=dataset.iloc[:,0:3].values
y=dataset.iloc[:,3].values
#Tratamiento de variablesFaltantes
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
#datos categoricos 
from sklearn import preprocessing
label_encoder_x=preprocessing.LabelEncoder()
x[:,0]=label_encoder_x.fit_transform(x[:,0])
y=label_encoder_x.fit_transform(y)
"""funciona pero no es la mejor forma pero se deaja
como muestra de su funcionamen se debe combertir a bar dummyes"""
#bariables dummy
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct= ColumnTransformer(
        [("one_hot_encoder",OneHotEncoder(categories="auto"),[0])],
        remainder="passthrough"
        )
x=np.array(ct.fit_transform(x),dtype=np.float)

#dividir data set in trainin y test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
#escalando datos 
from sklearn .preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.fit_transform(x_test)

