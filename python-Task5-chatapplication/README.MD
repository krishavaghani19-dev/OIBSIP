# 💬 Real-Time Chat Application (Python Socket Programming)

A simple **Real-Time Chat Application** built using **Python Socket Programming** and **Multithreading**. The application enables two or more clients to communicate over a local network using **localhost**. It supports real-time message exchange, timestamps, client connection notifications, and graceful disconnection handling.

---

# 📌 Project Overview

This project consists of two Python programs:

- **Server (`server.py`)** – Listens for incoming client connections and manages message broadcasting.
- **Client (`client.py`)** – Connects to the server and allows users to send and receive messages in real time.

The application demonstrates the fundamentals of **socket programming**, **network communication**, and **multithreading** in Python.

---

# ✅ Beginner Tier Features

- ✔ Server script listens for incoming client connections
- ✔ Client script connects to the server
- ✔ Real-time bidirectional messaging between connected clients
- ✔ Messages displayed with a timestamp (e.g., `[14:35] Alice: Hello`)
- ✔ Graceful disconnection handling with notifications
- ✔ Runs on the same machine using **localhost (127.0.0.1)**

---

# 🛠 Technologies Used

- Python 3
- Socket Programming
- Threading
- Datetime Module

---

# 📂 Project Structure

```
Chat-Application/
│
├── server.py
├── client.py
└── README.md
```

---

# 📦 Requirements

No external libraries are required.

The project uses only Python's built-in modules:

- socket
- threading
- datetime

---

# ▶ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Chat-Application.git
```

### 2. Open the project folder

```bash
cd Chat-Application
```

### 3. Start the server

```bash
python server.py
```

Output:

```
Server started...
```

### 4. Open another terminal and run the client

```bash
python client.py
```

Open multiple client windows to chat with each other.

---

# 💻 Sample Chat

### Client 1

```
Enter your name: Alice

[14:35] Alice: Hello!
```

### Client 2

```
Enter your name: Bob

[14:35] Alice: Hello!
[14:36] Bob: Hi Alice!
```

---

# ⚙ Configuration

Server Configuration

```python
HOST = "127.0.0.1"
PORT = 12345
```

- **HOST:** `127.0.0.1` (localhost)
- **PORT:** `12345`

Both server and client should use the same host and port values.

---

# 📡 How It Works

1. The server starts and listens for incoming client connections.
2. A client connects to the server using localhost.
3. The server requests the client's name.
4. Messages sent by one client are broadcast to all other connected clients.
5. Every message includes a timestamp and the sender's name.
6. When a client disconnects, the server notifies the remaining connected clients.

---

# ✅ Feature Checklist

| Feature | Status |
|---------|--------|
| Server listens for client connections | ✅ |
| Client connects to server | ✅ |
| Real-time bidirectional communication | ✅ |
| Timestamped messages | ✅ |
| Graceful disconnection handling | ✅ |
| Runs on localhost | ✅ |

---

# 🚀 Future Improvements

- Graphical User Interface (Tkinter or PyQt5)
- Private messaging
- Group chat support
- File sharing
- Emoji support
- Message history
- User authentication
- Chat encryption
- Online user list
- Multiple chat rooms

---

# 👨‍💻 Author

**Krisha Vaghani**

Python | Socket Programming | Networking

---

# 📄 License

This project was developed for educational and internship purposes.

You are free to use, modify, and enhance this project.
