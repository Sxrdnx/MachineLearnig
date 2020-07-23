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
#prueba de git 
