from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle, Ellipse
from random import random as r
from functools import partial
from kivy.lang import Builder


class StressCanvasApp(App):

    def add_rects(self, label, wid, count, *largs):
        with wid.canvas:
                Color(1, 1, 1, 1)
                #Rectangle(pos=(10,150), size=(180, 400))
                Ellipse(pos=(10,150), size=(180, 180))

    def add_rects2(self, label, wid, count, *largs):
        with wid.canvas:
                Color(1, 1, 1, 1)
                Rectangle(pos=(210,150), size=(180, 400))

    def add_rects3(self, label, wid, count, *largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:
            for x in range(count):
                Color(r(), 1, 1, mode='hsv')
                Rectangle(pos=(410,150), size=(180, 400))

    def reset_rects(self, label, wid, *largs):
        label.text = '0'
        wid.canvas.clear()

    def build(self):
        wid = Widget()

        label = Label(text='0',size_hint= (0.5,1),font_name='fonts/Lcd.ttf',font_size='40dp')

        btn_add1 = Button(text='Position 1',
                            on_press=partial(self.add_rects, label, wid, 1))

        btn_add2 = Button(text='Position 2',
                            on_press=partial(self.add_rects2, label, wid, 1))

        btn_add3 = Button(text='Position 3',
                            on_press=partial(self.add_rects3, label, wid, 1))

        btn_reset = Button(text='Reset', size_hint= (0.5,1),
                           on_press=partial(self.reset_rects, label, wid))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add1)
        layout.add_widget(btn_add2)
        layout.add_widget(btn_add3)
        layout.add_widget(btn_reset)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    StressCanvasApp().run()