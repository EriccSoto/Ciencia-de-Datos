# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
UA: Ciencia de Datos

"""
import pandas as pd
  
path = './iris/iris.data'
df = pd.read_csv(path, header=None)#si hubiese un encabezado sería  df = pd.read_csv(path)

#Agregamos nombres a las comlumnas:
names = ['sepal_length', 'sepal_width', 'petal_lenght', 'petal_width', 'class']
df.columns = names
print(df)