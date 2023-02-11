#!/usr/bin/python3

import zmq 
import json

def mensajeria():

    # Crear contexto. Conectar socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    # Resivir mensajes

    while True:
        mesaje = socket.recv().decode("utf-8")

        informacion = mansaje.split('/')

        opcion = informacion[0]

        if opcion == 'Registar':




        print("Enviado: %s" % mansaje)
        clientes_str = ''
        for clientes in servidor["clientesbanco"]:
            clientes_str += clientes[mansaje] + ", "

        socket.send_string(clientes_str)









try:
    with open('Datos_Bancarios.json', 'a') as file:
        servidor = json.load(file)
except FileNotFoundError:
    servidor = {}
    servidor['clientesbanco'] = []
    
    servidor['clientesbanco'].append({
        'nombre': self.usuario.get()})
    
    
    with open('Datos_Bancarios.json', 'w') as file:
        json.dump(servidor, file, indent=4)
    


if __name__ == '__main__':
    mensajeria()