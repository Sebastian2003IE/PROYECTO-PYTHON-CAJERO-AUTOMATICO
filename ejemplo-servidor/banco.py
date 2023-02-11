#!/usr/bin/python3



#
#   Hello World client in Python
#   Connects REQ socket to tcp://<ipserver>:5555
#   Sends "Hello" to server, expects "World" back
#

import json
import zmq


#------#------#------#------#------#------#------#------#------#

# Contexto. Conectar socket
context = zmq.Context()
#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://10.0.2.4:5555")

#------#------#------#------#------#------#------#------#------#

# enviar mensaje e imprimir contenido del archivo
informacion_requerrida = input("Que desea saber:\n>>> ")

while informacion_requerrida != "nada":
    
    socket.send_string(informacion_requerrida)

    message = socket.recv().decode("utf-8")

    print(message)

    informacion_requerrida = input("Que desea saber:\n>>> ")





