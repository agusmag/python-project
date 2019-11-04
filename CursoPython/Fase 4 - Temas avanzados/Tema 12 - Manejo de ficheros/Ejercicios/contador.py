#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:29:48 2019

@author: agustinm
"""

from io import open
import sys

archivo = open('contador.txt', 'a+')
archivo.seek(0)

contenido = archivo.readline()

if len(contenido) == 0:
    contenido = "0"
    archivo.write(contenido)
    
archivo.close()

#Transformar el texto a un número

try:
    contador = int(contenido)
    #En función de lo que el usuario quiera...
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1
    print("El contador actual es:", contador)
    
    #Finalmente volvemos a escribir los cambios en el archivo
    archivo = open('contador.txt', 'w')
    archivo.write( str(contador) )
    archivo.close()
except:
    print("Error: fichero corrupto")
