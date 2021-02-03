
print("Client side communication") 
import socket
host= socket.gethostname()
port = 9234
socket = socket.socket()
socket.connect((host,port))
file=open("img.jpg","wb")
while True:
    data=socket.recv(1024)
    while data:
        file.write(data)
        data=socket.recv(1024)
    file.close()
    break
socket.close()
print("File received successfully")
