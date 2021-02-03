print("\tClient Server Calculator")
print("############################################################")
print("If you want to stop calculation,enter x while giving input")
print("############################################################")

import socket
print("\t\t\t Client side communication ")
host = socket.gethostname()  
port = 9987
socket = socket.socket()  
socket.connect((host, port)) 
while True:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    operator = input("Enter the operator")    
    message = a +','+ b +','+operator
    socket.send(message.encode())
    if a =='x' or b == 'x' or operator == 'x':
        break
    data= socket.recv(2000).decode()
    print(int(a),operator,int(b),"=",data)

print('Connection Closed')
socket.close()
