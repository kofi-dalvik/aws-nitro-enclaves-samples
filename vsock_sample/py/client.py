import socket, hashlib

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

def recvall(conn: socket.socket) -> str:
    res: str = ''
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            break

def send(conn: socket.socket, msg: str) -> str:
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    
    conn.send(send_length)
    conn.sendall(message)
    return conn.recv(2048).decode(FORMAT)
    
    

if __name__ == "__main__":
    connection: socket.socket = connnect()
    msg: str = 'Hello World!' * (1024 * 1024)
    res: str = send(connection, msg=msg)
    assert res == hashlib.sha256(msg.encode(FORMAT)).hexdigest()
    print(res)
    send(connection, DISCONNECT_MESSAGE)