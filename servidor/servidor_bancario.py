#!/usr/bin/python3

import zmq 
import json

def registrar(informacion)

    # Contenido del mensaje

    nombre = informacion[1]
    contra = informacion[2]
    # primer_ingreso = informacion[3] #  falta agregar

    try:
        with open('Datos_Bancarios.json') as file:
            archivo = json.load(file)
            archivo['clientesbanco'].append({
                'nombre': nombre,
                'contra': contra
            })

        with open('Datos_Bancarios.json', 'w') as file: 
            json.dump(archivo, file, indent=4)

        

    except FileNotFoundError:
        archivo = {}
        archivo['clientesbanco'] = []
        archivo['clientesbanco'].append({
            'nombre': nombre,
            'contra': contra
        })

    socket.send_string("Anadido a la base de datos")

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
            registrar(informacion)


if __name__ == '__main__':
    mensajeria()
