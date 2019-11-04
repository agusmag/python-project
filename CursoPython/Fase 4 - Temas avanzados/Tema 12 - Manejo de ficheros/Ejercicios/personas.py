#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:22:19 2019

@author: agustinm
"""

from io import open

archivo = open('personas.txt', 'r', encoding="utf8")
lineas = archivo.readlines()
archivo.close()

personas = []

for linea in lineas:
    campos = linea.replace("\n", "").split(';') #Para reemplazar los \n #Para separar los campos
    persona = { "id":campos[0], "nombre":campos[1], "apellido":campos[2], "nacimiento":campos[3] }
    personas.append(persona)
    
    for p in personas:
        print(" (id={}) {} {} => {}".format(p['id'], p['nombre'], p['apellido'], p['nacimiento']))
    
print(personas)