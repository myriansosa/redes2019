from socket import *
from contanstes import *
from pickle import*
from paquete import*

def create_socket():
	UDPsocket=socket(AF_INET, SOCK_DGRAM)
	return UDPsocket
	
	
def rdt_send(): 
    data= input('ingrese mensaje') 
    return data.encode('utf-8')

def make_pkt(dato):
	pkt = packet(SOURCE_PORT,RECEIVER_PORT, dato)
	return pkt
	
def udp_send(socket, pkt):
	data = dumps(pkt)
	socket.sendto(data,(RECEIVER_IP, RECEIVER_PORT))
	
def close_socket(socket):
	socket.close()
	
		
if __name__ == "__main__":
    cliente= create_socket()
    while True :
        data=rdt_send() #recibe paquete del emisor rdt=tranferencia confiable
        pkt=make_pkt(dato)#crea el paquete en la capa de transporte
        udp_send(cliente, pkt)
    close_socket(cliente)
   
