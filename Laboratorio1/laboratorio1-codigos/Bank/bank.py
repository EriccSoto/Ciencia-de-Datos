# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 08:32:08 2024

@author: ericc
"""

import pandas as pd

path = './bank+marketing/bank/bank-full.csv'


# Lee el archivo CSV especificando el delimitador y el carácter de comillas
datos = pd.read_csv(path, delimiter=';', quotechar='"')

# Agrega nombres a las columnas si es necesario
names = ['edad', 'empleo', 'estado_civil', 'educación', 'impago', 'saldo', 'hipoteca', 'préstamo', 'contacto', 'día', 'mes', 'duración', 'campaña', 'pdays', 'previous', 'poutcome', 'suscripción']
datos.columns = names

# Imprime las primeras filas del DataFrame
print(datos)
