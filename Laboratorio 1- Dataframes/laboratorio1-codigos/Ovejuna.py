# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:51:56 2024

@author: ericc
"""

import requests

# URL del libro en formato de texto plano
url = "https://www.gutenberg.org/cache/epub/60198/pg60198.txt"

# Realizar la solicitud HTTP para obtener el contenido del libro
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Almacenar el contenido del libro como una cadena
    book_content = response.text
    print(book_content)
    
    
    """
    # Imprimir las primeras 500 líneas (o todo el contenido si hay menos de 200 líneas)
    for line in lines[:500]:
        print(line)
    """
else:
    print(f"Error {response.status_code}: No se pudo descargar el libro.")
