from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
import Platinum

class TouchFunctionsLightCircle(Widget):
    """
        - This class need to make a lightcircle which will follow each position of the platinum

        - Minimum size is 100px, each scroll changes the size by 40px too
        - You can use scroll function on slider without resizing the circle
        - Circle is moving position only if you move the mouse by holding the click
    """

    coord_x_plat = Platinum.TouchFunctionsPlatinum.coord_x_plat
    coord_y_plat = Platinum.TouchFunctionsPlatinum.coord_y_plat
    coord_x_circle = NumericProperty(360)
    coord_y_circle = NumericProperty(300)
    zoom = NumericProperty(100)

    def on_touch_up(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                self.zoom += 40

            elif touch.button == 'scrollup':
                self.zoom -= 40
                if self.zoom <= 100:  # Minimum Size
                    self.zoom = 100


class MyLightCircleApp(App):
    intensity_value = NumericProperty(0.1)


if __name__ == '__main__':
    MyLightCircleApp().run()
