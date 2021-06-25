# Importar las librerias para los sockets e información para figuras

import socket
from _thread import *
import pickle


server = "localhost" #Se utiliza "localhost" para identificar la red local donde se almacena el servidor
port = 5555 #Los puertos que se abrirán para que puedan conectarse al servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #La primera parte representa la conexión y la segunda representa la string del server

#Probar la conexión del servidor
try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(2) #son las conexiones posibles
print("Esperando la conexión, servidor iniciado")


#Función para leer la posición de los jugadores dentro del juego
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

#Función que transforma la posición inicial pasandolo de string a una tupla
def make_pos(tup):
    return str(tup[0])+","+str(tup[1])

#La posición inicial de los jugadores
pos = [(0,0),(100,100)]


#Se realiza el cambio de información cliente servidor, determinando la posición de los jugadores
def threaded_cliente(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data


            if not data:
                print ("Desconectado")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Recibiendo: ", data)
                print ("Enviando: ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("Conexión Perdida")
    conn.close()

#Determinar los jugadores conectados y la ip donde se conectan
currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Conectado a:", addr) #addr representa la ip a la cual se conectan los clientes

    start_new_thread (threaded_cliente, (conn,currentPlayer))
    currentPlayer += 1