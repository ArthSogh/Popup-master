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
from kivy.core.window import Window
from kivy.properties import StringProperty

class kivy_super_box(BoxLayout):

    def save_opacity(self):
        Light1 = 1*int(button_box.slider.value)/100
        Light2 = 0
        Light3 = 0
        print(Light1)

    def follow(self):
        self.label = Label()
        Window.bind(mouse_pos=lambda w, p: setattr(self.label, 'text', str(p)))

class lightApp(App):

    def build(self):
        return kivy_super_box()

if __name__ == '__main__':
    lightApp().run()