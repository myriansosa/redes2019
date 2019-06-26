from socket import *
from contanstes import *
from pickle import*

def create_socket(address, port):
	servidor = socket(AF_INET, SOCK_DGRAM)
	servidor.bind((address, port))
	return servidor

def print_message(message):
    print (message)

def rdt_send():#baja datos desde la capa de aplicaciones
	data = input('ingrese mensaje: ')
	return data.encode('utf-8')


def udt_rcv(socket):
	packet = loads(socket.recv(2048))
	return packet
	
def extract(packet): # estrae el encabezado del paquete, para solo quedarse con los datos
	return packet
	
def deliver_data(data): #envia los datos a la capa de aplicacion
    print (data)

def close_socket(socket):
    socket.close()

if __name__ == "__main__":
	emisor=create_socket(RECEIVER_IP, RECEIVER_PORT)
	while 1:
		packet=rdt_send()
		packet=udt_rcv(socket)
		paquete=extract(packet)
		data=deliver_data (data)
	close_socket(cliente)
