from constants import *
from socket import*


def create_socket(adrres, port):
    UDPsocket = socket(AF_INET, SOCK_DGRAM)
	return UDPsocket

def print_message(message):
	data = input('Ingrese mensaje: ')
    print (message)

def make_pkt(data):
	pkt = packet(SENDER_PORT, NETWORK_PORT, data)
	return pkt

def udp_send(socket, receiver packet):
	dato = dumps((receiver, packet))
	socket.sendto(dato, (NETWORK_IP, NETWORK_PORT))

'''
def recv_message(UDPsocket):
	UDPsocket.close()
	# IMPLEMENTAR
'''

def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
	# Creamos el socket
	emisor = crete_socket()
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, cliente))
	# Iteramos indefinidamente
	while True:
		# Leemos el mensaje desde teclado
		daa = rdt_send()
		# Hacemos el paquete
		paquete = make_pkt(data)
		# Establecemos el destinatario
		destinatario = (RECEIVER_IP, RECEIVER_PORT)
		# Enviamos el mensaje
		udp_send(cliente,destinatario, paquete)
	close_socket(cliente)
