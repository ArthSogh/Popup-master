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
        on_release:  root.start_server(), root.disable_me()

""")
server = None
HOST_ADDR = "localhost"
HOST_PORT = 5466
client_value = " "
clients = []
clients_valueS = []
player_data = []

class Main_Screen(BoxLayout):

    def disable_me(self):
        self.btn.disabled = True

    def start_server(self):
        global server, HOST_ADDR, HOST_PORT  # code is fine without this

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        global server, client_value, clients

        client_msg = " "

        # send welcome message to client
        client_value = self.client_connection.recv(4096).decode()

        if len(clients) < 2:
            client_connection.send("welcome1".encode())
        else:
            client_connection.send("welcome2".encode())

        clients_valueS.append(client_value)

        if len(clients) > 1:
            sleep(1)

            # send opponent name
            clients[0].send(("opponent_name$" + clients_valueS[1]).encode())
            clients[1].send(("opponent_name$" + clients_valueS[0]).encode())
            # go to sleep

        while True:
            data = client_connection.recv(4096).decode()
            if not data:
                break

        client_connection.close()

class TouchApp(App):
    def build(self):
        return Main_Screen()


if __name__ == "__main__":
    TouchApp().run()