from socket import *
#importamos modulos para trabajar con sockets

#Creamos un objeto sockets para el servidor
def create_UDPsocket():
	UDPsocket=socket(AF_INET, SOCK_DGRAM)
	return UDPsocket
	
#va de capa de aplicacion a capa de transporte
def rdt_send():
	data = input('ingrese mensaje: ')
	return data.encode('utf-8')
	
def make_pkt(data):
	return data

#Nos conectamos al servidor	
def udp_send(socket, data):
	#El primero es la IP y el segundo el puerto de conexion del servidor
	socket.sendto(data, ('localhost', 20000))
	
def close_socket(socket):
	UDPsocket.close()
	
if __name__ == "__main__":
	cliente=create_UDPsocket()
	while 1:
		data=rdt_send()
		paquete=make_pkt(data)
		udp_send(cliente, data)
	close_socket(cliente)
	
