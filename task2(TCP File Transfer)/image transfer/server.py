print("Server side communication") 
import socket
host= socket.gethostname()
port = 9234
socket = socket.socket()
socket.bind((host,port))
print("Waiting for connection..")
socket.listen(2)
c,addr=socket.accept()
#print("Connected with",addr)
print("Connected with client")
file=open("data_to_be_sent\img.jpg","rb")
data=file.read(1024)
print("sending file ...")
while data:
    c.send(data)
    data=file.read(1024)
file.close()
print("File sent successfully")
