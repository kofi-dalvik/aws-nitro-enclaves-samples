import socket

address: tuple = (socket.gethostbyname(socket.gethostname()), 5005)

def recv(sock: socket.socket) -> bytes:
    data: bytearray = bytearray()
    while True:
        chunk = sock.recv(1024)
        print(f'Received chunk data: {chunk.decode()}')
        if not chunk:
            break
        data.extend(chunk)
    return bytes(data)

def main(data: bytes) -> bytes:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    for i in range(0, len(data), 10):
        sock.send(data[i:10])
    sock.send(b'Done')
    
    res: bytes = recv(sock=sock)
    print('Server Res: ', res.decode())
    sock.close()
    return res
    
    
    
    
if __name__ == "__main__":
    main(b'hello world' * 10)