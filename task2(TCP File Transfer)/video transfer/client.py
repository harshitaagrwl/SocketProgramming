print("Client side communication") 
import socket
host= socket.gethostname()
port = 9876
socket = socket.socket()
socket.connect((host,port))
file=open("harshi.mp4","wb")
#250 mb=250000000 bytes
while True:
    data=socket.recv(250000000)
    while data:
        file.write(data)
        data=socket.recv(250000000)
    file.close()
    break
print("File received successfully")
