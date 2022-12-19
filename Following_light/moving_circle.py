from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class TouchFunctions(Widget):
    """
        - Minimum size is 100px, each scroll changes the size by 40px too
        - You can use scroll function on slider without resizing the circle
        - Circle is moving position only if you move the mouse by holding the click
    """

    coord_x = NumericProperty(360)
    coord_y = NumericProperty(300)
    zoom = NumericProperty(100)

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                self.zoom += 40

            elif touch.button == 'scrollup':
                self.zoom -= 40
                if self.zoom <= 100:  # Minimum Size
                    self.zoom = 100

    def on_touch_move(self, touch):
        if not touch.is_mouse_scrolling:
            if (touch.pos[0] < self.coord_x + self.zoom/2
                    and touch.pos[1] < self.coord_y + self.zoom/2):
                if (touch.pos[0] > self.coord_x - self.zoom/2
                        and touch.pos[1] > self.coord_y - self.zoom/2):
                    self.coord_x = (touch.pos[0])
                    self.coord_y = (touch.pos[1])


class IntensitySlider(BoxLayout):
    @staticmethod
    def montre():
        print('test')


class MyMovingApp(App):
    intensity_value = NumericProperty(0.1)


if __name__ == '__main__':
    MyMovingApp().run()
