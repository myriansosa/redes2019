from constantes import *
from socket import *

def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	return UDPsocket

def rdt_send():
	data = input('mensaje')
	return UDPsocket

def make_pkt(data):
	pkt = packet(SENDER_IP, RECEIVER_PORT,data)
	return pkt

def udp_send(socket, receiver, paquete):
	dato= dumps(receiver, packet)
	socket.sendto((NETWORK_IP, NETWORK_PORT),data)

def close_socket(socket, signal, frame):
	print("\n\rCerrando socket")
	socket.close()
	exit(0)

if __name__ == '__main__':
	emisor = create_socket()
	signal.signal(signal.SIGINT, partial(close_socket, cliente))

	while True:
		data = rdt_send()
		pkt = make_pkt(data)
		receiver = (RECEPTOR_IP, RECEPTOR_PORT)
		udp_send = (emisor, receiver, pkt)
	close_socket

