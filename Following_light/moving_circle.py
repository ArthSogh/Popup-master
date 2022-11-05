from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App




class Touch_functions(Widget):
    '''
        - Minimum size is 40px, each scroll changes the size by 40px too
        - You can use scroll function on slider without resizing the circle
        - Circle is moving position only if you move the mouse by holding the click
    '''

    coord_x = NumericProperty(100)
    coord_y = NumericProperty(100)
    zoom = NumericProperty(100)

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                self.zoom += 40

            elif touch.button == 'scrollup':
                self.zoom -= 40
                if self.zoom <=0:    #I did it because scolling button don't accept negative numbers
                    self.zoom =1

    def on_touch_move(self, touch):
        self.coord_x = (touch.pos[0])
        self.coord_y = (touch.pos[1])
        pass

class MyMovingApp(App):
    intensity_value = NumericProperty(0.1)

if __name__ == '__main__':
    MyMovingApp().run()