from constants import *
from pickle import *
from socket import *
from packet import *


def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGARM)
	UDPsocket.bin((RECEIVER_IP, RECEIVER_PORT))
	return UDPsocket

def extract(packet):
	data = packet.get_data()
	return data

def deliver_data(data):
	print(data)

def rdt_rcv(sock):
	data=sock.recv(2048)
	paquete=loads(data) # decodifica 
	return paquete

def close_socket(socket, signal, frame):
	print ("\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
	# Creamos el socket "receiver"
	servidor = create_socket()
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, receptor))
	# Imprimimos el cartel "Listo para recibir mensajes..."
	print('Listo para recibir mensaje: ')

	# Iteramos indefinidamente
	while True:
		# Recibimos un paquete de la red
		paquete = rdt_rcv(receptor)
		# Extraemos los datos
		data = extrac(packet)
		# Entregamos los datos a la capa de aplicacion
		deliver_data(data)
	close_socket(servidor)	
