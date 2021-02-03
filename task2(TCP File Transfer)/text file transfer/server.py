print("Server side communication") 
import socket

host= socket.gethostname()
port = 9900
socket = socket.socket()
socket.bind((host,port))
print("Waiting for connection..")
socket.listen(2)

while True:
    c,addr=socket.accept()
    print("Connected with client")
    filename=c.recv(1024).decode()
    file=open(filename,"w")
    c.send("File name received".encode())
    data=c.recv(1024).decode()
    #print("file data received")
    file.write(data)
    c.send("File received successfully".encode())
    file.close()
    c.close()
    
    
