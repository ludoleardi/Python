import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket per ricezione
my_address = ('0.0.0.0', 8000)
server.bind(my_address)

next_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket per invio
next_address = ('192.168.1.123', 8000)

#ricevo
text_received, address = server.recvfrom(4096)
print(f'Ricevuto {text_received.decode()} da {address}')

next_sock.sendto(text_received, next_address) #invio al prossimo

next_sock.close()
server.close()