#!/usr/bin/python3

import zmq 
import json

def registrar(informacion, socket):

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
        with open('Datos_Bancarios.json', 'w') as file: 
            json.dump(archivo, file, indent=4)

    socket.send_string("Anadido a la base de datos")
    print('El usuario {} ha sido anadido a la base de datos'.format(nombre))
def mensajeria():

    # Crear contexto. Conectar socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    # Resivir mensajes

    while True:
        mensaje = socket.recv()
        
        mensaje = mensaje.decode("utf-8")
        informacion = mensaje.split('/')
        opcion = informacion[0]
        
        if opcion == 'Registrar':
            registrar(informacion, socket)


if __name__ == '__main__':
    mensajeria()
