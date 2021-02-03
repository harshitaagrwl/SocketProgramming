import socket
print("Server Side Communication : ")
print("Waiting for connection....")

host = socket.gethostname()
port = 9999  

server_socket = socket.socket()  
server_socket.bind((host, port))

# configure how many client the server can listen simultaneously
server_socket.listen(2)
c, addr = server_socket.accept()  
print("Connection from: " + str(addr))
while True:
    data = c.recv(1024).decode()
    if not data:
        # if data is not received break
        break
    print("Message from client: " + str(data))
    data = input(' -> ')
    c.send(data.encode())  
c.close()
