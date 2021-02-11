https://pythondiario.com/2015/01/simple-programa-clienteservidor-socket.html


## Código del cliente
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
# www.pythondiario.com
 
import socket
import sys
 
# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('localhost', 10001)
print >>sys.stderr, 'conectando a %s puerto %s' % server_address
sock.connect(server_address)
try:
     
    # Enviando datos
    message = raw_input("Pon el mensaje: ")
    print >>sys.stderr, 'enviando "%s"' % message
    sock.sendall(message+'#')
 
    # Buscando respuesta
    amount_received = 0
    amount_expected = len(message)
     
    while amount_received < amount_expected:
        data = sock.recv(19)
        amount_received += len(data)
        print >>sys.stderr, 'recibiendo "%s"' % data
 
finally:
    print >>sys.stderr, 'cerrando socket'
    sock.close()
```

### Código servidor

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor
# www.pythondiario.com
 
import socket
import sys
 
# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de socket y puerto
server_address = ('localhost', 10001)
print >>sys.stderr, 'empezando a levantar %s puerto %s' % server_address
sock.bind(server_address)
# Escuchando conexiones entrantes
sock.listen(1)

while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse'
    connection, client_address = sock.accept()
 
    try:
        print >>sys.stderr, 'concexion desde', client_address
 
        # Recibe los datos en trozos y reetransmite

        data = ""
        while True:
			datarec = connection.recv(1)
			print >>sys.stderr, str(datarec)
			if datarec=="#":
				break
			else:
				data+=datarec
        print >>sys.stderr, 'recibido "%s"' % data
        if data:
			print >>sys.stderr, 'enviando mensaje de vuelta al cliente'
			connection.sendall(data)
        else:
			print >>sys.stderr, 'no hay mas datos', client_address
			break
             
    finally:
		print >>sys.stderr, 'Cerrando Conexion...'
		# Cerrando conexion
		connection.close()
```
