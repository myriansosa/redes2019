from constants import *
from pickle import *
from socket import *
from packet import *


def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((RECEIVER_IP, RECEIVER_PORT))
	return UDPsocket

def extract(packet):
	data = Packet.get_data()
	print(data)
	return data

def deliver_data(data):
	print(data)

def rdt_rcv(sock):
	data=sock.recv(2048)
	paquete=loads(data) # decodifica 
	print(paquete)
	return paquete


def close_socket(socket, signal, frame):
	print ("\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
	# Creamos el socket "receiver"
	receptor = create_socket()
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, receptor))
	# Imprimimos el cartel "Listo para recibir mensajes..."
	print('recibiendo mensaje: ')

	# Iteramos indefinidamente
	while True:
		# Recibimos un paquete de la red
		paquete = rdt_rcv(receptor)
		# Extraemos los datos
		data = extrac(packet)
		#print(data.get_data)
		# Entregamos los datos a la capa de aplicacion
		deliver_data(data)
	close_socket(cliente)
