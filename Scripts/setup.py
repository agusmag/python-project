#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:44:10 2019

@author: agustinm
"""

from setuptools import setup

#Para poder distribuir un paquete hay que indicar un par de parámetros
setup(
    name="paquete",
    version="0.1",
    description="Este es un paquete de ejemplo",
    author="Agustin Magliano",
    author_email="yo@test.com",
    url="https://test.com",
    script=[],
    packages=["paquete","paquete.chau","paquete.hola"]    
)

#Ahora hay que crear el distribuible
#Desde la termina se usa el comando python3 setup.py dist

#Para instalar un paquete (se usa el gestor de python pip3)
#pip3 install [paquete.taz]