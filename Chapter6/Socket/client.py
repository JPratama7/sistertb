# client .py
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# connection to hostname on the port .
s.connect((host, port))

stasiun = input("Berikan tujuan Perjalanan : ")
s.send(stasiun.encode("utf8"))
# Receive no more than 1024 bytes
tm = s.recv(1024)
s.close()
print(tm.decode('utf8'))
