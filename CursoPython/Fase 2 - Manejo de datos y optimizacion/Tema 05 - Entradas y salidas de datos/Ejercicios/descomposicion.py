#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:26:39 2019

@author: agustinm
"""

import sys

if len( sys.argv ) == 2:
    numero = int( sys.argv[1])
    
    if numero < 0 or numero > 9999:
        print("Error, parámetro inválido")
        print("Ejemplo: descomposicion.py [0-9999]")
    else:
        #Lógica
        cadena = str(numero)
        longitud = len( str(numero) )
        for i in range(longitud):
            #Se va tomando el índice multiplicado por 10 elevado al índice
            # Esto me permite hacer:
            # cadena[i] * 10^i => Por ej 4 * 10^1 , 5 * 10^2, etc
            print("{:04d}".format( int(cadena[longitud - 1 - i]) * 10 ** i))
else:
    print("Error, faltan parámetros")
    print("Ejemplo: descomposicion.py [0-9999]")