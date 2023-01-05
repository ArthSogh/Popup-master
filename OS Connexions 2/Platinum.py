#---------------------------------------------------------------------------CLIENT 1
import threading

from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from subprocess import Popen, PIPE

import socket
#
# host, port = ('localhost', 5566)
# socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cl2_label = ""
cl1_label = "Positionnnnn"

# network client platinum
client = None
HOST_ADDR = "localhost"
HOST_PORT = 5466
class TouchFunctionsPlatinum(Widget):
    """
    - Red Circle is representing the platinum,by moving it I need to send an order to LightCircle file, to move the
    following light.
    """

    coord_x_plat = NumericProperty(200)
    coord_y_plat = NumericProperty(400)
    zoom = NumericProperty(200)

    def connect(self):
        global cl2_label
        self.zoom_label.text = "Label of client 1: " + cl1_label
        self.connect_to_server(cl1_label)

    def connect_to_server(self,label_value):
        global client, HOST_ADDR, HOST_PORT
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST_ADDR, HOST_PORT))
            print('connected')
            client.send(label_value.encode())  # Send my name to server after connecting

            # start a thread to keep receiving message from server
            # do not block the main thread :)
            threading._start_new_thread(self.receive_message_from_server, (client, "m"))

        except Exception as e:
            print('did  not work')
            title="ERROR!!!",
            message="Cannot connect to host: "

    def receive_message_from_server(self,sck, m):
        global cl2_label, cl1_label
        while True:
            from_server = str(sck.recv(4096).decode())
            print(from_server)
            if not from_server:
                print("breaken")
                break

            elif from_server.startswith("opponent_name$"):
                cl2_label = from_server.replace("opponent_name$", "")
                print("oppenent result" + cl2_label)
                self.lbl_opponent_value.text = "Opponent: " + cl2_label


        sck.close()

    # try:
    #     socket.connect((host, port))
    #     print("Client Connecté ! ")
    #
    # except ConnectionRefusedError:
    #     print("Serveur echoué !")

    def on_touch_move(self, touch):
        # print(touch)

        # data = str(self.coord_x_plat)
        # data = data.encode("utf8")
        # socket.sendall(data)

        if not touch.is_mouse_scrolling:
            if (touch.pos[0] < self.coord_x_plat + self.zoom/2
                    and touch.pos[1] < self.coord_y_plat + self.zoom/2):
                if (touch.pos[0] > self.coord_x_plat - self.zoom/2
                        and touch.pos[1] > self.coord_y_plat - self.zoom/2):
                    self.coord_x_plat = (touch.pos[0])
                    self.coord_y_plat = (touch.pos[1])
                    print(self.coord_x_plat)


    def btn_touch_up(self):
        # if (self.btn.text == "Turn ON lights"):
        #    self.btn.text = "Turn OFF lights"
        Popen(['python', 'LightCircle.py'], stdin=PIPE, stdout=PIPE)



class MyPlatinumApp(App):
    intensity_value = NumericProperty(0.1)

if __name__ == '__main__':
    MyPlatinumApp().run()
