import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.129', 5000)

while True:
    text = input('Scrivi un messaggio: ')
    if text == 'exit':
        break
    text_b = text.encode()
    s.sendto(text_b, server_address)
    text_received, address = s.recvfrom(4096)
    print(f'Ricevuto {text_received.decode()} da {address}')

s.close()