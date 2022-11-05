from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from random import random

class Gamescreen(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self)
        self._keyboard.bind(on_key_down=self._on_key_down)

        with self.canvas:
            Rectangle(pos=(0,0),size=(100,100))

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self,keyboard,keycode,text,modifiers):
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]
        newx = currentx
        currenty = currenty
        if text =='w':
            currenty += 1


class MoveApp(App):
    def build(self):
        return Gamescreen()

if __name__ == '__main__':
    MoveApp().run()