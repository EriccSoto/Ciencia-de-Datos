# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:12:06 2024

@author: ericc
"""

import requests
import pandas as pd

# Lista de URLs de libros
book_urls = [
    "https://www.gutenberg.org/cache/epub/74282/pg74282.txt",
    "https://www.gutenberg.org/cache/epub/74273/pg74273.txt",
    "https://www.gutenberg.org/cache/epub/74274/pg74274.txt",
    "https://www.gutenberg.org/cache/epub/74275/pg74275.txt",
    "https://www.gutenberg.org/cache/epub/74276/pg74276.txt",
    "https://www.gutenberg.org/cache/epub/74277/pg74277.txt",
    "https://www.gutenberg.org/cache/epub/74278/pg74278.txt",
    "https://www.gutenberg.org/cache/epub/74279/pg74279.txt",
    "https://www.gutenberg.org/cache/epub/74280/pg74280.txt",
    "https://www.gutenberg.org/cache/epub/74281/pg74281.txt",
]

# Crear listas para almacenar los textos y los títulos
texts = []
titles = []

# Descargar el contenido de cada libro y extraer el título
for url in book_urls:
    response = requests.get(url)
    if response.status_code == 200:
        # Almacenar el contenido del libro como una cadena
        book_content = response.text
        
        # Buscar la línea que contiene el título
        start_index = book_content.find('Title: ')
        end_index = book_content.find('\n', start_index)
        title = book_content[start_index + len('Title: '):end_index].strip()
        
        # Almacenar el contenido y el título en las listas
        texts.append(book_content)
        titles.append(title)
    else:
        texts.append(None)
        titles.append(None)

# Crear el DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Text": texts
})

# Mostrar el DataFrame
print(df)  # Imprime las primeras filas del DataFrame para ver el resultado
