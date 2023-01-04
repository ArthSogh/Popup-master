#---------------------------------------------------------------------------CLIENT 2
import threading

from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

import socket

cl2_label = ""
cl1_label = ""

# network client platinum
client = None
HOST_ADDR, HOST_PORT = ('localhost', 5566)

#
# host,port = ('',5566)
#
# socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socket.bind((host,port))
# print("le serveur est démarré !")
#
# socket.listen()
# conn, adress = socket.accept()
# print("Un client vient de se connecter...")


class TouchFunctionsLightCircle(Widget):
    """
        - This class need to make a lightcircle which will follow each position of the platinum

        - Minimum size is 100px, each scroll changes the size by 40px too
        - You can use scroll function on slider without resizing the circle
        - Circle is moving position only if you move the mouse by holding the click
    """

    # coord_x_plat = Platinum.TouchFunctionsPlatinum.coord_x_plat
    # coord_y_plat = Platinum.TouchFunctionsPlatinum.coord_y_plat
    # data = conn.recv(1024)
    # data.decode("utf8")
    # print(data)
    #
    # txt = data

    coord_x_plat = NumericProperty(100)
    coord_y_plat = NumericProperty(100)
    coord_x_circle = NumericProperty(360)
    coord_y_circle = NumericProperty(300)
    zoom = NumericProperty(100)

    def connect(self):
        global cl2_label
        self.zoom_label["text"] = "Label of client 1: " + cl2_label
        self.connect_to_server(cl2_label)

    def connect_to_server(self,label_value):
        global client, HOST_PORT, HOST_ADDR, cl2_label
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST_ADDR, HOST_PORT))
            client.send(label_value.encode())  # Send name to server after connecting

            # start a thread to keep receiving message from server
            # do not block the main thread :)
            threading._start_new_thread(self.receive_message_from_server, (client, "m"))

        except Exception as e:
            title="ERROR!!!",
            message="Cannot connect to host: "

    def receive_message_from_server(self,sck, m):
        global cl2_label, cl1_label
        while True:
            from_server = str(sck.recv(4096).decode())

            if not from_server:
                break

            if from_server.startswith("welcome"):
                if from_server == "welcome1":
                    print(
                            "Server says: Welcome " + cl2_label + "! Waiting for player 2"
                    )
                elif from_server == "welcome2":
                    print(
                            "Server says: Welcome " + cl2_label + "! Game will start soon"
                    )

            elif from_server.startswith("opponent_name$"):
                cl1_label = from_server.replace("opponent_name$", "")
                self.lbl_opponent_value["text"] = "Opponent: " + cl1_label


        sck.close()

    def on_touch_up(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                self.zoom += 40

            elif touch.button == 'scrollup':
                self.zoom -= 40
                if self.zoom <= 100:  # Minimum Size
                    self.zoom = 100


class MyLightCircleApp(App):
    intensity_value = NumericProperty(0.1)


if __name__ == '__main__':
    MyLightCircleApp().run()
