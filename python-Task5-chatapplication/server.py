import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []

print("Server started...")

def broadcast(message, sender=None):
    for client in clients:
        if client != sender: 
            try:
                client.send(message.encode())
            except:
                pass

def handle(client):
    while True:
        try:
             message = client.recv(1024).decode()

            # Client disconnected
             if not message:
              raise ConnectionResetError

             print(f"Received: {message}")
             broadcast(message, client)
        except:
            if client in clients:
                index = clients.index(client)
                name = names[index]
                clients.remove(client)
                names.remove(name)
                client.close()
                broadcast(f"Server: {name} left the chat.")
                print(name, "disconnected")
            break

while True:
    client, address = server.accept()
    print("Connected:", address)

    client.send("NAME".encode())
    name = client.recv(1024).decode()


    clients.append(client)
    names.append(name)

    print(name, "joined")

    broadcast(f"{name} joined the chat.")

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()