#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:17:48 2019

@author: agustinm
"""

import sys

if len( sys.argv ) == 3:
    filas = int( sys.argv[1] )
    columnas = int( sys.argv[2] )
    
    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("Error, los argumentos son incorrectos")
        print("Ejemplo tabla.py [1-9] [1-9]")
    else:
        #Lógica
        for i in range(filas):
            print("")
            for j in range(columnas):
                print(" * ", end='') #El end evita hacer salto de linea
else:
    print("Error, Argumentos incorrectos")
    print("Ejemplo tabla.py [1-9] [1-9]")