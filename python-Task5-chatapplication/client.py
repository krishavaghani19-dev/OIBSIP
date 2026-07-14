import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "NAME":
                client.send(name.encode())
            else:
                print(message)

        except:
            print("Disconnected from server.")
            client.close()
            break

def write():
    while True:
        try:
            text = input()

            # Exit command
            if text.lower() == "exit":
                client.shutdown(socket.SHUT_RDWR)
                client.close()
                break

            current_time = datetime.now().strftime("%H:%M")
            message = f"[{current_time}] {name}: {text}"

            client.send(message.encode())

        except:
            break

threading.Thread(target=receive).start()
threading.Thread(target=write).start()