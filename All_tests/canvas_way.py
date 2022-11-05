from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial

class canvaApp(App):

    def add_rects(self,label,wid,count,*largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:
            Color(r(),1,1,mode='hsv')
            Rectangle(pos=(100,100), size=(20,20))

    def build(self):
        wid = Widget()

        label = Label(text='0')

        btn_add = Button(text='+1',on_press=partial(self.add_rects,label,wid,1))

        layout = BoxLayout(size_hint=(1,None), height=50)
        layout.add_widget(btn_add)

        root=BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

if __name__ == '__main__':
    canvaApp().run()