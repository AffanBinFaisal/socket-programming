import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('---Socket created---')

hostname = socket.gethostname()
print(f'Hostname: {hostname}')

host = socket.gethostbyname(hostname)
print(f'Host: {host}')

PORT = 12347
ADDR = (host,  PORT)

s.bind(ADDR)

print(f'---Socket bound to port {ADDR}---')

s.listen()


def handle_client(c):
    while True:
        data_recv = c.recv(1024).decode()
        if not data_recv:
            clients.remove(c)
            c.close()
            print('User Disconnected')
            break
        print(f'Client: {data_recv}')
        for client in clients:
            if client != c:
                client.send(data_recv.encode())


clients = list()

while True:
    c, addr = s.accept()
    print('User joined')
    clients.append(c)
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode())
    thread = threading.Thread(target=handle_client, args=(c,))
    thread.start()
