from socket import *
from contanstes import *
from pickle import*
from paquete import *

def create_socket(address, port):
	servidor = socket(AF_INET, SOCK_DGRAM)
	servidor.bind((address, port))
	return servidor

def print_message(message):
    print (message)


def rdt_recv(socket):
	datos = socket.recv(2048)
	packet = loads(datos)
	return packet
	
def extract(packet): 
	data = packet.get_data()
	return data
	
def deliver_data(data): #envia los datos a la capa de aplicacion
    print (data)

def close_socket(socket):
    socket.close()

if __name__ == "__main__":
	servidor=create_socket(RECEIVER_IP, RECEIVER_PORT)
	print_message('servidor corriendo')
	while 1:
		packet = rdt_recv(servidor)
		data = extract(packet)
		deliver_data(data)
	close_socket(servidor)
