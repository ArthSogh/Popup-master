import socket

host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))
    print("Client Connecté ! ")

    data = "Bonjour je suis le client ! :"
    data = data.encode("utf8")
    socket.sendall(data)

except ConnectionRefusedError:
    print("Serveur echoué !")
finally:
    socket.close()