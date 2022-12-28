from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from subprocess import Popen, PIPE
import rpyc

#c = rpyc.classic.connect("localhost")

import socket

host, port = ('localhost',5566)
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    socket.bind((host,port))
    print("Client demarré")
except:
    print("Connexion échue")
finally:
    socket.close()


class TouchFunctionsPlatinum(Widget):
    """
    - Red Circle is representing the platinum,by moving it I need to send an order to LightCircle file, to move the
    following light.
    """

    coord_x_plat = NumericProperty(100)
    coord_y_plat = NumericProperty(100)
    zoom = NumericProperty(200)

    """def affiche(self,code):
        def telep(y):
            return y+50

        fn = c.teleport(telep)
        fn(self.coord_x_plat)

        print("Position en temps réel en x : ", self.coord_x_plat, file=c.modules.sys.stdout)
        print("Position en temps réel en x +1 : ", fn(self.coord_x_plat), file=c.modules.sys.stdout)
        return fn(self.coord_x_plat)"""

    def on_touch_move(self, touch):
        """def telep(y):
            return y+50"""

        print(self.coord_x_plat)
        x = self.coord_x_plat
        print('x',x)
        """print("Position en temps réel en x : ",x, file = c.modules.sys.stdout)
        #rlist = c.modules.builtins.list(x)  # remote list

        fn = c.teleport(telep)
        fn(x)
        print("Position en temps réel en x +1 : ",fn(x), file = c.modules.sys.stdout)"""

        if not touch.is_mouse_scrolling:
            if (touch.pos[0] < self.coord_x_plat + self.zoom/2
                    and touch.pos[1] < self.coord_y_plat + self.zoom/2):
                if (touch.pos[0] > self.coord_x_plat - self.zoom/2
                        and touch.pos[1] > self.coord_y_plat - self.zoom/2):
                    self.coord_x_plat = (touch.pos[0])
                    self.coord_y_plat = (touch.pos[1])
                    #self.affiche(92)


    def btn_touch_up(self):
        # if (self.btn.text == "Turn ON lights"):
        #    self.btn.text = "Turn OFF lights"
        Popen(['python', 'LightCircle.py'], stdin=PIPE, stdout=PIPE)


class MyPlatinumApp(App):
    intensity_value = NumericProperty(0.1)

if __name__ == '__main__':
    MyPlatinumApp().run()
