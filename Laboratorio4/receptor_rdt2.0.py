from constantes import *
from paquete import *
from network import *

def create_socket():#(servidor)
    UDPsocket = socket(AF_INET, SOCK_DGRAM)
    UDPsocket.bind((RECEPTOR_IP, RECEPTOR_PORT)) #es para saber donde tiene que escuchar el ip y purta del archivo constantes
    return UDPsocket

def extract(packet):
    data=Paquete.get_data()
    return data

def deliver_data(message):
    print(message)

def rdt_rcv(socket):#recibe la data de la red, obtengo dato, descomprime data , obtiene el pkt y emisor
	data =socket.recvfrom(2048)
	emisor, pckt=loads(data) #descomprimo con load
	return (emisor, pckt)

def corrupto(paquete):
    if paquete.set_checksum() == 0:
        return True
    else:
        return False

def make_pkt(receptor, servidor,datos):
    paquete = Paquete(receptor, emisor, datos, 0) #indicamos de dnd sale y a dond tiene q ir
    ckecksum = calcular_checksum(paquete)
    paquete.set_checksum(ckecksum)
    return paquete


def udp_send(socket,emisor, paquete): #envia el paq
    datos = dumps(emisor, confirmacion) #comprime
    socket.sento((NETWORK_IP, NETWORK_PORT), datos) #ENVI datos a la red
    return datos

def close_socket(socket, signal, frame):
    print ("\rCerrando socket")
    socket.close()
    exit(0)


if __name__ == "__main__":
    servidor=create_socket()
    # Creamos el socket "receiver"

    # Registramos la senial de salida
    signal.signal(signal.SIGINT, partial(close_socket, servidor))
    # Imprimimos el cartel "Listo para recibir mensajes..."
    print("Listo para recibir mensajes...")

    # iniciamos la variable secuencia en 0
    secuencia = 0
    # iteramos indefinidamente
    while True:
        (emisor, pckt) = rdt_rcv(servidor)
        if corrupto(0):
            sndpkt=make_pkt(servidor, receptor, datos)#pkt1=crear_paquete('NAK')
            paquete=rdt_rcv(servidor, sndpkt)       #enviar_paquete(pkt1)
        elif recv_paquete and not corrupto:		#else:
            data=extract(paquete)				#pkt2=crear_paquete('ack')
            #Extraemos los datos				#enviar_paquete(pkt2)
            deliver_data(data)					#msj=extraer_msj(pkt)
            #Entregamos los datos a la cap de aplicacion #enviar_mensaje(msj)
            paquete=make_pkt("ACK",checksum)       #sumar 1
            udt_send(paquete)
    close_socket()
