import kivy
import cv2
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

class Widgets0(Widget):
    def btn(self):
        show_popup()

class P2(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return Widgets0()

    def show_opencv(self):
        img = cv2.imread("Image/ecran.jpg", 1)
        img = cv2.rectangle(img, (320, 100), (360, 160), (255, 0, 0), 2)

        cv2.imshow("Image Test", img)


def show_popup():
    show = P2()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()

if __name__ == "__main__":
    MyApp().run()