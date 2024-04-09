import socket, hashlib
import vsock

SERVER = (16, 5005) # SET to None if running locally

if __name__ == "__main__":
    connection: socket.socket = vsock.connect(address=SERVER)
    msg: str = 'Hello World!' * (1024)
    vsock.send(connection, msg=msg)
    res: str = vsock.response_recv(connection)
    assert hashlib.sha256(res.encode(vsock.FORMAT)).hexdigest() == hashlib.sha256(msg.encode(vsock.FORMAT)).hexdigest()
    vsock.disconnect(connection)