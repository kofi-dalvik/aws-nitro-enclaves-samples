import socket, threading, hashlib

PORT = 5005
HEADER = 64
FORMAT = "utf-8"
BUFFER_SIZE = 2048
DISCONNECT_MESSAGE = "!disconnect!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def recvall(conn: socket.socket, msg_length: int):
    msg = ''
    while len(msg) < msg_length:
        num_bytes = min(BUFFER_SIZE, msg_length - len(msg))
        m = conn.recv(num_bytes).decode(FORMAT)
        # print('Size: ', num_bytes, 'Message: ', m)
        msg += m
    return msg

def handle_client(conn: socket.socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            print('Message length: ', msg_length)
            msg = recvall(conn, msg_length)
            # print('Message received: ', msg)
            
            if msg == DISCONNECT_MESSAGE:
                break
                
            # print(f"[{addr}] {msg}")
            print('Processing request...')
            print('Message: ', msg)
            res: str = hashlib.sha256(msg.encode(FORMAT)).hexdigest()
            conn.send(msg.encode(FORMAT))
            
    conn.close()
    print(f"[CONNECTION CLOSED] {addr} disconnected.")
    
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start()