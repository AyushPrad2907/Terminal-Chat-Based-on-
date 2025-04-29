import socket
import threading

nickname = input("Enter your nickname: ")
HOST = '127.0.0.1'  # Use loopback address to connect to your own laptop
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            print(msg)
        except:
            print("[ERROR] Connection closed.")
            client.close()
            break

def write():
    while True:
        msg = f'{nickname}: {input()}'
        client.send(msg.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()
