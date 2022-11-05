from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle, Ellipse
from random import random as r
from functools import partial
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.switch import Switch
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty,ObjectProperty,NumericProperty,ListProperty

class Touch(Widget):

    btn = NumericProperty(0)

    def on_touch_down(self, touch):
        print("Mouse Down",touch)

        print(touch.pos[1]/1000)
        pass

    def on_touch_up(self, touch):
        #print("Mouse Up",touch)
        pass

    def on_touch_move(self, touch):
        #self.btn.opacity = (touch.pos[1] / 1000)*2
        self.btn = (touch.pos[1] / 1000)*2
        #print("Mouse Moove",touch)
        pass




class inside(BoxLayout):
    pass

#class Grid(GridLayout):
   # pass

#class inside2(BoxLayout):
#    pass

class screen3x3App(App):

    list_color = ListProperty([1,1,1,0])
    intensities = ListProperty([0]*9)
    sizes = ListProperty([0]*9)


if __name__ == '__main__':
    screen3x3App().run()