from kivy.app import App
from kivy.uix.widget import Widget

#Builder.load_file('circletest.kv')

class CircleWidget(Widget):

    def __init__(self, **kwargs):
        self.size= [50,50]
        self.pos = [100,50]
        self.r = 0
        super(CircleWidget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x,touch.y):
            self.pos = [self.pos[1],self.pos[0]]
            self.r = 1.0


class sliderApp(App):
    def build(self):
        parent = Widget()
        w = CircleWidget()
        parent.add_widget(w)
        return parent

if __name__ == '__main__':
    sliderApp().run()