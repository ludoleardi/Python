import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_address = ('127.0.0.1', 5000)
s.bind(my_address)

while True:
    text_received, address = s.recvfrom(4096)
    print(f'Ricevuto {text_received.decode()} da {address}')
    s.sendto(b'OK', address)

s.close()