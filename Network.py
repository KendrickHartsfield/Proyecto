#Llamar a las librerías de socket y pickle para la creación de los sockets del servidor y envíar los datos de imagen del juego/servidor
import socket
import pickle

#Crear la clase "Network" que funcionará como red para el juego/servidor
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

#Función que obtiene la posición de los jugadores dentro del cliente
    def getPos(self):
        return self.pos

#Función que determina si la conexión del servidor con la red fue exitosa
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

#Función para enviar y recibir los datos entre juego/servidor
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

