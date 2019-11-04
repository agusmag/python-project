#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:48:43 2019

@author: agustinm
"""
import random
import math

def leer_numero(ini, fin, mensaje):
    
    while True:
        try:
            valor = int( input(mensaje) )
        except:
            print("Error: Número no válido")
        else:
            if valor >= ini and valor <= fin:
                break
    
    return valor

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20] ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Hacia arriba [2]Hacia abajo [3]Normal")
    
    lista = []
    
    for i in range(numeros):
        numero = random.uniform(0, 101)
        if modo == 1:
            print("{} => {}".format(numero, math.ceil(numero)))
            numero = math.ceil(numero)
        elif modo == 2:
            print("{} => {}".format(numero, math.floor(numero)))
            numero = math.floor(numero)
        elif modo == 3:
            print("{} => {}".format(numero, round(numero)))
            numero = round(numero)

        lista.append(numero)
    
    return lista

generador()