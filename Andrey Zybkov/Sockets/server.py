import socket

sock = socket.socket()

sock.bind(('127.0.0.1', 9090))

sock.listen(10)

conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()

conn1.send(b"Connected")
conn2.send(b"connected")

while True:

    conn1.send(conn2.recv(100))
    conn2.send(conn1.recv(100))