# server .py
import atexit
import socket
import time

print("Running server.....")
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)


# establish a connection

# Close socket when exit
@atexit.register
def handler():
    serversocket.close()


schd = {"gambir": ["Gambir", "08:00"], "bandung": ["Bandung", "09:30"], "yogyakarta": ["Yogyakarta", "11:15"],
    "surabaya": ["Surabaya", "13:45"], "malang": ["Malang", "15:20"], }

while True:
    sock, addr = serversocket.accept()
    strFinal = "Data Stasiun tidak ditemukan"
    data = sock.recv(1024).decode('utf8').lower()
    jadwal = schd.get(data)
    if jadwal is not None:
        strFinal = f"Jadwal perjalanan kereta api di stasiun {jadwal[0]} datang pada jam {jadwal[1]}."

    sock.send(strFinal.encode('utf8'))
    sock.close()
