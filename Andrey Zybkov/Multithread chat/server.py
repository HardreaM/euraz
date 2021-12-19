import threading
import socket

sock = socket.socket()

sock.bind(('127.0.0.1', 9090))

sock.listen(10)

conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()

conn1.send(b"Connected")
conn2.send(b"connected")

def send1(sock, event_for_wait, event_for_set):
    while True:

        conn1.send(conn2.recv(400))

def send2(sock, event_for_wait, event_for_set):
    while True:

        conn2.send(conn1.recv(400))

# init events
e1 = threading.Event()
e2 = threading.Event()

# init threads
t1 = threading.Thread(target=send1, args=(sock, e1, e2), daemon=True)
t2 = threading.Thread(target=send2, args=(sock, e2, e1), daemon=True)

# start threads
t1.start()
t2.start()

# join threads to the main thread
t1.join()
t2.join()
