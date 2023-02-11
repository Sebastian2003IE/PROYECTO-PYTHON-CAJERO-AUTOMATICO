#!/usr/bin/python3


from time import sleep 
import json
import zmq 

#------#------#------#------#------#------#------#------#------#

# Contexto. Conectar socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#------#------#------#------#------#------#------#------#------#

#archivo .json
servidor = {}
servidor['clientesbanco'] = [] 

with open('Datos_Bancarios.json') as file:
    servidor = json.load(file)

    
#------#------#------#------#------#------#------#------#------#

# Mensajeria. resivir mensaje y envio info de archivo

while True:
    message = socket.recv().decode("utf-8")
    print("Enviado: %s" % message)
    clientes_str = ''
    for clientes in servidor["clientesbanco"]:
        clientes_str += clientes[message] + ", "

    socket.send_string(clientes_str)

    



