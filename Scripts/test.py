#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:30:16 2019

@author: agustinm
"""

#Importo el módulo saludos (en este caso está en el mismo directorio)
#Si el módulo está en otro directorio, debe importarse el módulo sys
#Por ejemplo: 
import sys

sys.path.insert(1,'./Modulos')
import saludos
#Si quiero directamente importar la función, uso from [modulo] import [función]
#from saludos import saludar (o por ejemplo la clase Saludo)
#from saludos import * #También puedo usar el *

#Para referirnos a los métodos del módulo, debo referirme al mpodulo como una clase
#saludos.saludar()
#saludar()
s = saludos.Saludo();

#TODO ESTO ES SI NO SE USAN PAQUETES, SIEMPRE USAR PAQUETES
