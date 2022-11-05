from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App


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
        print("Mouse Moove",touch)
        pass

class Inside2(BoxLayout):
    pass

class screen3x3App(App):

    list_color = ListProperty([1,1,1,0])
    intensities = ListProperty([0]*9)
    sizes = ListProperty([0]*9)



if __name__ == '__main__':
    screen3x3App().run()