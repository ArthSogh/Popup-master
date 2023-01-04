import tkinter as tk
import socket
import threading
from time import sleep

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

Builder.load_string("""
<Main_Screen>:
    btn:btn
    orientation: 'vertical'
    Button:
        id: btn
        size_hint: 1,0.2
        text: "Open Light's Screen"
        on_release:  root.start_server()

""")
server = None
HOST_ADDR = "localhost"
HOST_PORT = 8080
client_name = " "
clients = []
clients_names = []
player_data = []

class Main_Screen(BoxLayout):

    def start_server(self):
        global server, HOST_ADDR, HOST_PORT  # code is fine without this

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.AF_INET)
        print(socket.SOCK_STREAM)

        server.bind((HOST_ADDR, HOST_PORT))
        server.listen(5)  # server is listening for client connection
        print("passed")
        threading._start_new_thread(self.accept_clients, (server, " "))


    def accept_clients(self,the_server, y):
        while True:
            if len(clients) < 2:
                client, addr = the_server.accept()
                clients.append(client)

                # use a thread so as not to clog the gui thread
                threading._start_new_thread(self.send_receive_client_message, (client, addr))


    def send_receive_client_message(self,client_connection, client_ip_addr):
        global server, client_name, clients, player_data, player0, player1

        client_msg = " "

        # send welcome message to client
        client_name = self.client_connection.recv(4096).decode()

        if len(clients) < 2:
            client_connection.send("welcome1".encode())
        else:
            client_connection.send("welcome2".encode())

        clients_names.append(client_name)

        if len(clients) > 1:
            sleep(1)

            # send opponent name
            clients[0].send(("opponent_name$" + clients_names[1]).encode())
            clients[1].send(("opponent_name$" + clients_names[0]).encode())
            # go to sleep

        while True:
            data = client_connection.recv(4096).decode()
            if not data:
                break

            # get the player choice from received data
            player_choice = data[11 : len(data)]

            msg = {"choice": player_choice, "socket": client_connection}

            if len(player_data) < 2:
                player_data.append(msg)

            if len(player_data) == 2:
                # send player 1 choice to player 2 and vice versa
                dataToSend0 = "$opponent_choice" + player_data[1].get("choice")
                dataToSend1 = "$opponent_choice" + player_data[0].get("choice")
                player_data[0].get("socket").send(dataToSend0.encode())
                player_data[1].get("socket").send(dataToSend1.encode())

                player_data = []

        # find the client index then remove from both lists(client name list and connection list)
        # idx = get_client_index(clients, client_connection)
        # del clients_names[idx]
        # del clients[idx]
        client_connection.close()

class TouchApp(App):
    def build(self):
        return Main_Screen()


if __name__ == "__main__":
    TouchApp().run()