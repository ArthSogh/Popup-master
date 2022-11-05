from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle, Ellipse
from random import random as r
from functools import partial
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.switch import Switch
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, NumericProperty


class screen_slide(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    counter = NumericProperty(0)

    def addition(self):
        print("Num prop : ", str(self.counter))
        self.counter += 1

    def btn(self):
        print("Name: ", self.name.text, "Email:", self.email.text)
        self.name.text = ""
        self.email.text = ""

class slide_rectApp(App):
    def build(self):
        return screen_slide()

if __name__ == '__main__':
    slide_rectApp().run()