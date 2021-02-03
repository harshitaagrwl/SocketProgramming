import socket
print("Client side communication ")
host = socket.gethostname()  
port = 9999  
client_socket = socket.socket()  
client_socket.connect((host, port)) 
msg = input(" -> ")  
while msg.lower().strip() not in ['bye','thankyou','thanks','error solved','issue resolved']:
    client_socket.send(msg.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    print('Message from server: ' + data)  # show in terminal
    msg = input(" -> ")  
client_socket.close()  

