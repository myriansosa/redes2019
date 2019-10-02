from paquete import *

if __name__ == "__main__":
	message = input('Ingrese e mensaje a enviar: ')
	pkt = Packet(2000, 2001, message)
	print(pkt.get_source())
	print(pkt.get_receiver())
	print(pkt.get_long())
	checksum = calculate_checksum(pkt)
	print('la primer comprobación da: ', checksum)
	pkt.set_checksum(checksum)
	new_checksum = calculate_checksum(pkt)
	print('la segunda comprobación da: ', new_checksum)
	
