from constants import *
from socket import*


def create_socket():
    UDPsocket = socket(AF_INET, SOCK_DGRAM)
	return UDPsocket

def rdt_send():
	data = input('Ingrese mensaje: ')
    return (data.encode('utf-8'))

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
	cliente = create_socket()
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, cliente))
	# Iteramos indefinidamente
	while True:
		# Leemos el mensaje desde teclado
		data = rdt_send()
		# Hacemos el paquete
		pkt = make_pkt(data)
		# Establecemos el destinatario
		receiver = (RECEIVER_IP, RECEIVER_PORT)
		# Enviamos el mensaje
		udp_send(cliente,receiver, pkt)
	close_socket(cliente)
