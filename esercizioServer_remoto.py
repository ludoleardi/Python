import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_address = ('0.0.0.0', 5000)
s.bind(my_address)

while True:
    text_received, address = s.recvfrom(4096)
    print(f'Ricevuto {text_received.decode()} da {address}')
    text = input('Scrivi un messaggio: ')
    if text == 'exit':
        break
    text_b = text.encode()
    s.sendto(text_b, address)

s.close()