# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:29:31 2024

@author: ericc
"""
import requests  # Importa la biblioteca requests para hacer solicitudes HTTP

# Primer bloque de código
url = 'https://jsonplaceholder.typicode.com/users'  # Define la URL de la API desde donde se obtendrán los datos
respuesta = requests.get(url)  # Realiza una solicitud GET a la URL
print(respuesta.json())  # Imprime la respuesta en formato JSON

# Segundo bloque de código
import pandas as pd  # Importa la biblioteca pandas para el manejo de datos

respuesta = requests.get(url)  # Realiza nuevamente una solicitud GET a la URL
if respuesta.status_code == 200:  # Verifica si la solicitud fue exitosa (código de estado 200)
    datos = respuesta.json()  # Convierte la respuesta JSON en un diccionario de Python
    df = pd.DataFrame(datos)  # Convierte el diccionario en un DataFrame de pandas
    print(df.head())  # Imprime las primeras filas del DataFrame
else:
    print(f"Error al obtener los datos: {respuesta.status_code}")  # Imprime un mensaje de error si la solicitud no fue exitosa
