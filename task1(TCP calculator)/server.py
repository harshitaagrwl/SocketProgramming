print("\tServer Side Communication : ")
import socket

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a//b

host= socket.gethostname()
port = 9987
socket = socket.socket()
socket.bind((host,port))
print("Waiting for connection")
socket.listen(2)
c, addr = socket.accept()  
#print("Connection from: " + str(addr))
print("Connected with client")
while True:
    msg=c.recv(2000).decode()
    msg= msg.split(",")
    a = msg[0]
    b = msg[1]
    op = msg[2]
    if a == 'X' or b == 'X' or op == 'X':
        break
    if op=="+":
        result= add(int(a),int(b))
        c.send(str(result).encode())

    elif op=="-":
        result= sub(int(a),int(b))
        c.send(str(result).encode())

    elif op=="*":
        result= multiplication(int(a),int(b))
        c.send(str(result).encode())

    elif op=="/":
        result= division(int(a),int(b))
        c.send(str(result).encode())

print('Connection Closed')
c.close()
