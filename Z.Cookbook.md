## Recetario/Cookbook

# DRAFT / VERSION 0.0

## ¿Como saber la versión de python que esatams usando?

import sys

if sys.version 

### Usando fechas

>>> import utime
>>> utime.time() # Epocs time: Segundos desde 1,1,1970 (GMT)
>>> utime.localtime(utime.time()) # tupla con formato (year,month,day,hour,minute,seconds,day of week, day of year)
>>> utime.localtime(utime.time()+3600) # Sumamos la hora para tiempo localtime


### Conversión de Epoch a fecha


Donde hemos usado la función time.ctime para convertir el formato de fecha Epoch (segundos desde el 1 de enero de 1970)que se usa en el sistema a un formato más legible

time.ctime(epocs)

## ¿Qué versión de micropython tengo instalada?

Cuando arranca la placa aparece en la descripción. Podemos provocar un reset con ctrl+D

´´´python
>>> import os
>>> os.uname()
´´´