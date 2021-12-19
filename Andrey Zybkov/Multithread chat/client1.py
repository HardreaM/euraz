import socket
import threading

sock = socket.socket()

sock.connect(('127.0.0.1', 9090))
    
def getter(sock, event_for_wait, event_for_set):
    while True:

        data = sock.recv(400).decode("UTF-8")
        print("Client says:", data)

def sender(sock, event_for_wait, event_for_set):
    while True:
        
        data = input()
        sock.send(bytes(data, encoding='UTF-8'))


# init events
e1 = threading.Event()
e2 = threading.Event()

# init threads
t1 = threading.Thread(target=getter, args=(sock, e1, e2), daemon=True)
t2 = threading.Thread(target=sender, args=(sock, e2, e1), daemon=True)

# start threads
t1.start()
t2.start()

# join threads to the main thread
t1.join()
t2.join()
