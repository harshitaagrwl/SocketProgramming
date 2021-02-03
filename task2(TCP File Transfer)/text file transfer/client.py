print("client side communication")
import socket

host= socket.gethostname()
port = 9900
socket = socket.socket()
socket.connect((host,port))
print("Connected to server")
file=open("data_to_be_sent/data.txt","r")
data=file.read()
#sending the name of file to the server,
#so that it can save the data with the same file name
socket.send("data.txt".encode())
msg=socket.recv(1024).decode()
print(msg)
socket.send(data.encode())
msg=socket.recv(1024).decode()
print(msg)
file.close()
socket.close()

