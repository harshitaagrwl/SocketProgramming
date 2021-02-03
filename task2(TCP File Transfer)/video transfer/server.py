print("Server side communication") 
print("Server can send file upto 250mb")
#250 mb=250000000 bytes
import socket
host= socket.gethostname()
port = 9876
socket = socket.socket()
socket.bind((host,port))
print("Waiting for connection..")
socket.listen(2)
c,addr=socket.accept()
#print("Connected with",addr)
print("Connected with client")
file=open("data_to_be_sent\harshi.mp4","rb")
data=file.read(250000000)
print("sending file ...")
while data:
    c.send(data)
    data=file.read(250000000)
file.close()
print("File sent successfully")
