import socket

sock = socket.socket()

sock.connect(('127.0.0.1', 9090))

print(sock.recv(100).decode("UTF-8"))

while True:
    
    
    data = input("Me: ")
    sock.send(bytes(data, encoding='UTF-8'))
    data = sock.recv(100).decode("UTF-8")
    print("Client says:", data)