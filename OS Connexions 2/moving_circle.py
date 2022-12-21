from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window


class Touch_functions(Widget):
    '''
        - Minimum size is 100px, each scroll changes the size by 40px too
        - You can use scroll function on slider without resizing the circle
        - Circle is moving position only if you move the mouse by holding the click
    '''

    coord_x = NumericProperty(360)
    coord_y = NumericProperty(300)
    zoom = NumericProperty(100)

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                self.zoom += 40

            elif touch.button == 'scrollup':
                self.zoom -= 40
                if self.zoom <=100:    #Minimum Size
                    self.zoom =100

    def on_touch_move(self, touch):
        if not touch.is_mouse_scrolling:
            if touch.pos[0] < self.coord_x + self.zoom / 2 and touch.pos[1] < self.coord_y + self.zoom / 2:
                if touch.pos[0] > self.coord_x - self.zoom / 2 and touch.pos[1] > self.coord_y - self.zoom / 2:
                    self.coord_x = (touch.pos[0])
                    self.coord_y = (touch.pos[1])
"""
    def on_touch_move(self, touch):
        print(self.coord_x,self.coord_y)
        if touch.pos[0]< self.coord_x + self.zoom/2 and touch.pos[1]<self.coord_y + self.zoom/2:
            if touch.pos[0] > self.coord_x - self.zoom/2 and touch.pos[1] > self.coord_y - self.zoom/2:
                self.coord_x = (touch.pos[0])
                self.coord_y = (touch.pos[1])
"""


class Intensity_Slider(BoxLayout):
    def montre(self):
        print('test')
    pass

class MyMovingApp(App):
    intensity_value = NumericProperty(0.7)


if __name__ == '__main__':
    MyMovingApp().run()