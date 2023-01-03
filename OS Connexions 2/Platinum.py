from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from subprocess import Popen, PIPE

import socket

host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class TouchFunctionsPlatinum(Widget):
    """
    - Red Circle is representing the platinum,by moving it I need to send an order to LightCircle file, to move the
    following light.
    """

    coord_x_plat = NumericProperty(100)
    coord_y_plat = NumericProperty(100)
    zoom = NumericProperty(200)

    try:
        socket.connect((host, port))
        print("Client Connecté ! ")

    except ConnectionRefusedError:
        print("Serveur echoué !")

    def on_touch_move(self, touch):
        # print(touch)

        data = str(self.coord_x_plat)
        data = data.encode("utf8")
        socket.sendall(data)

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
