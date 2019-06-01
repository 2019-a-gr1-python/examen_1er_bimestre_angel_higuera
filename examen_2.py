#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:56:35 2019

@author: tenshi
"""

import numpy as np
import pandas as pd
# 11) ¿Como crear una serie de una lista, diccionario o arreglo?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_lista = pd.Series(mylist) ## Respuesta
serie_array = pd.Series(myarr) ## Respuesta
serie_dic = pd.Series(mydict) ## Respuesta

# 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
# Transformar la serie en dataframe y hacer una columna indice
df_1 = pd.DataFrame(ser) ## Respuesta

# 13) ¿Como combinar varias series para hacer un DataFrame?
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

combinado_1=pd.DataFrame({'a': ser1,'b':ser2}) ## Respuesta

# 14) ¿Como obtener los items que esten en una serie A y no en una serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser3 = ser1 not in pd.Series(np.intersect1d(ser1,ser2)) ## Respuesta

# 15) ¿Como obtener los items que no son comunes en una serie A y serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser3 = pd.Series(np.intersect1d(ser1,ser2))

ser4 =pd.concat([ser1, ser2], axis=0)

# 16) ¿Como obtener el numero de veces que se repite un valor en una serie?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

# 17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

# 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?
ser = pd.Series(np.random.randint(1, 10, 35))
# shape(7,5)

ser2 = ser.reshape(7,5)

# 19) ¿Obtener los valores de una serie conociendo la posicion por indice?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

primero_a = ser.iloc[pos] ## Respuesta

# a e i o u
# 20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

ser4 =pd.DataFrame(pd.concat([ser1, ser2], axis=1)) ## Respuesta

# 21)¿Obtener la media de una serie agrupada por otra serie?
# groupby tambien esta disponible en series.
# 
frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())

#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64
# 
# 22)¿Como importar solo columnas especificas de un archivo csv?
# https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv

path = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'

data=pd.read_csv(
        path,
        usecols=['crim', 'zn'],
        index_col='crim'
        )  ## Respuesta