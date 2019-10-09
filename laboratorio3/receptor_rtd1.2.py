from constants import *
from packet import *
from constants import *
from network import *


def create_socket(address, port):
	UDPsocket = socket(AF_INET, SOCK_DGARM)
	UDPsocket.bin((address, port))
	return UDPsocket

def extract(packet):
	data = packet.get_data()
	return data

def rdt_rcv(sock):
	packet = loads(sock.recv(2048))
	return packet

def deliver_data(data):
	print(data)

def close_socket(socket, signal, frame):
	print ("\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
	# Creamos el socket "receiver"
	receptor = create_socket(RECEIVER_IP, RECEIVER_PORT)
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, receptor))
	# Imprimimos el cartel "Listo para recibir mensajes..."
	print('Listo para recibir mensaje: ')
	# Iteramos indefinidamente
	while True:
		# Recibimos un paquete de la red
		packet = rdt_rcv(receptor)
		data = extrac(packet)
		deliver_data(data)
	close_socket(servidor)
		
		# Extraemos los datos
		
		# Entregamos los datos a la capa de aplicacion
		
