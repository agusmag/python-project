#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:37:22 2019

@author: agustinm
"""

import sys

if len( sys.argv) == 3:
    # El primer argumento es el nombre del script como en bash.
    texto = sys.argv[1]
    repeticiones = int( sys.argv[2] )
    for r in range(repeticiones):
        print(texto)
else:
    print("Error, introduce los argumentos correctamente")
    print("Ejemplo: escribir_lineas.py 'Texto' 5")
     