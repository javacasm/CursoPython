6. ficheros

Ficheros de texto vs ficheros binarios

Serializacion de objetos

json



## numeros a bytes y bits

>>> n = 23
>>> n.bit_length()
5
>>> n = 2300
>>> n.bit_length()
12
>>> n.to_bytes(2,byteorder='big')
b'\x08\xfc'
>>> n.to_bytes(2,byteorder='little')
b'\xfc\x08'