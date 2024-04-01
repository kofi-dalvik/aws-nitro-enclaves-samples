import socket, time

address: tuple = (socket.gethostbyname(socket.gethostname()), 5005)

def recv(sock: socket.socket) -> bytes:
    data: bytearray = bytearray()
    while True:
        chunk = sock.recv(10)
        print(f'Received chunk data: {chunk.decode()}')
        if not chunk:
            break
        data.extend(chunk)
    return bytes(data)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    server.listen(5)
    print('Server listening on ', address)
    
    try:
        while True:
            connection, addr = server.accept()
            print(f'Connection from {addr} has been established')
            data: bytes = recv(sock=connection)
            print('Client Req: ', data.decode())
            time.sleep(3)
            connection.sendall(b'Hi world!')
            connection.close()
    except KeyboardInterrupt as ex:
        server.close()
    
    
if __name__ == "__main__":
    main()