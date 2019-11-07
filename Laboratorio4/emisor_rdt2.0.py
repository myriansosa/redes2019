from constantes import *
from socket import *
from paquete import *
from network import *

def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM) 
	return UDPsocket


def rdt_send():
    data=input('ingrese un mensaje:  ') #escribo mensaje a enviar
    return(data.encode('utf-8')) #codifico el mensaje 


def make_pkt(data):
    pkt = Paquete(EMISOR_PORT , RECEPTOR_PORT, data, 0)
    cksum = calcular_checksum(pkt)
    pkt.set_checksum(cksum)
    return pkt  
	


def udp_send(socket, mensaje, receiver): #data y reciber
	mensaje=dumps((receiver, mensaje))
	socket.sendto(mensaje, (NETWORK_IP,NETWORK_PORT))#con esto mando a la red  



def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
    # Creamos el socket
	cliente=create_socket() 
	
	signal.signal(signal.SIGINT, partial(close_socket, cliente))#esta funcion toma el socket al final
    # Iteramos indefinidamente
	while True:
        # Leemos el mensaje desde teclado 
		data=rdt_send() 
        # Hacemos el paquete
		paquete=make_pkt(data)
        # Establecemos el destinatario 
		destinatario = (RECEPTOR_IP, RECEPTOR_PORT)
        # Enviamos el mensaje 
		udp_send(cliente, paquete, destinatario) 
	close_socket(cliente)  
		
