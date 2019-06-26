from socket import *#importa toda la libreria de socket
from contanstes import *
from pickle import*

def create_socket(address, port):
	servidor=socket(AF_INET, SOCK_DGRAM)
	servidor.bind((address, port))
	return servidor
	
def print_message(message):
    print (message)
	
def rdt_send(socket): #recibe paquete del emisor rdt=tranferencia confiable
    packet= socket.recv(2048) #recibe datos con el buffer asignado 
    return packet

def make_pkt(data):
	pkt = packet(data,(SOURCE_PORT,RECEIVER_PORT))
	
def udp_send(socket, pkt):
	data = dumps(pkt)
	socket.sendto(data,(RECEIVER_IP, RECEIVER_PORT))
	
def close_socket(socket):
	UDPsocket.close()
	
		
if __name__ == "__main__":
    servidor= create_socket(RECEIVER_IP,SOURCE_PORT)
    print_message("servidor corriendo")
    while True :
        data=rdt_send(servidor) #recibe paquete del emisor rdt=tranferencia confiable
        pkt=make_pkt(data)#crea el paquete en la capa de transporte
        udp_send(emisor, pkt)
    close_socket(servidor)
   
