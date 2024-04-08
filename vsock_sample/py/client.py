import socket 

PORT = 5005
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!disconnect!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

def connnect():
    client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(conn: socket.socket, msg: str):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    
    conn.send(send_length)
    conn.send(message)
    # client.send(DISCONNECT_MESSAGE.encode(FORMAT))
    print(conn.recv(2048).decode(FORMAT))
    

if __name__ == "__main__":
    connection: socket.socket = connnect()
    send(connection, 'Hello World!')
    send(connection, DISCONNECT_MESSAGE)