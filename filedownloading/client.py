import socket
import threading
from tqdm import tqdm
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind(('192.168.0.133', 12346))

SERVER_ADDR = ('192.168.0.133', 12347)

client.connect(SERVER_ADDR)


def handle_response():
    with open('response.jpeg', 'wb') as file:
        data_recv = client.recv(1024).decode('utf-8', 'ignore').strip()
        str_file_size = str(data_recv.split('\n')[0])
        file_size = int(str_file_size)
        steps = (file_size // 1024) + 1
        with tqdm(total=steps, desc="Downloading File", unit="KB") as pbar:
            while True:
                data_recv = client.recv(1024)
                if not data_recv and pbar.n == steps:
                    client.close()
                    break
                file.write(data_recv)
                pbar.update(1)

thread = threading.Thread(target=handle_response, args=())
thread.start()
thread.join()