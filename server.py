import socket
import threading

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 5000
clients = []

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    print(f"[NEW] {addr} connected.")
    while True:
        try:
            msg = conn.recv(1024)
            if msg:
                broadcast(msg, conn)
        except:
            conn.close()
            clients.remove(conn)
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server running on {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
