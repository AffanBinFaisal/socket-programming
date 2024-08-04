import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind(('10.7.226.148', 12345))

SERVER_ADDR = ('10.7.226.148', 12347)

client.connect(SERVER_ADDR)

data_recv = client.recv(1024)
print('Server: ', data_recv.decode())


def handle_response():
    data_recv = client.recv(1024)
    print('Server: ', data_recv.decode())


thread = threading.Thread(target=handle_response, args=())
thread.start()

while True:
    # client.send(b'I am client')
    client.send(input('Enter a message: ').encode())
