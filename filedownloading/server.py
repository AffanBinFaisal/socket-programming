import socket
import threading
import os

def handle_client(c):
    try:
        with open('img.jpeg', 'rb') as file:
            file_size = os.path.getsize('img.jpeg')
            str_file_size = str(file_size)
            c.sendall(str_file_size.encode('utf-8') + b'\n')  # Send file size with newline delimiter

            while True:
                data = file.read(1024)
                if not data:
                    break
                c.sendall(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        c.close()

def start_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()

    print(f'---Socket bound to port {port}---')

    while True:
        try:
            c, addr = s.accept()
            print(f"Connection from {addr}")
            thread = threading.Thread(target=handle_client, args=(c,))
            thread.start()
        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == "__main__":
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    PORT = 12347
    start_server(host, PORT)
