import socket

#------------------------------------------------------
host,port = ('',5566)

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
print("le serveur est démarré !")

for i in range(5):
    print(i)
    socket.listen(5)
    conn, adress = socket.accept()
    print("Un client vient de se connecter...")


    data = conn.recv(1024)
    data.decode("utf8")
    print(data)

conn.close()
socket.close()
