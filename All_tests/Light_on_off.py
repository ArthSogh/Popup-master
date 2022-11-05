from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix import slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty


class LightApp(App):

    def add_rects1(self, button_box,*largs):
        with button_box.canvas.before:
            if self.btn1.state == 'down':
                Color(1, 1, 1, 1)
                Rectangle(pos=(293,400), size=(215, 127),orientation='horizontal')

            else:
                button_box.canvas.before.clear()


    def add_rects2(self, button_box,*largs):
        with button_box.canvas.before:
            if self.btn2.state == 'down':
                Color(1, 1, 1, 1)
                Rectangle(pos=(293,276), size=(215, 127),orientation='horizontal')
            else:
                button_box.canvas.before.clear()

    def add_rects3(self, button_box,*largs):
        with button_box.canvas.before:
            if self.btn3.state == 'down':
                Color(1, 1, 1, 1)
                Rectangle(pos=(293,149), size=(215, 127),orientation='horizontal')
            else:
                button_box.canvas.before.clear()


    def build(self):

        superbox = BoxLayout(orientation='vertical')
        button_box = BoxLayout(size_hint=(1, None), height=50)
        pos_box = BoxLayout(size_hint=(1, 1), height=50, orientation='vertical')

        image = Image(source='screen.png')
        superbox.add_widget(image)


        #self.button_pos1 = Button(text='Pos 1',pos_hint={"center_x": 0.5, "center_y": 0.5},on_press=partial(self.add_rects1, button_box))
        self.btn1 = ToggleButton(text='Pos1',pos_hint={"center_x": 0.5, "center_y": 0.5},on_press=self.add_rects1)
        self.btn2 = ToggleButton(text='Pos2',pos_hint={"center_x": 0.5, "center_y": 0.5},on_press=self.add_rects2)
        self.btn3 = ToggleButton(text='Pos3',pos_hint={"center_x": 0.5, "center_y": 0.5},on_press=self.add_rects3)


        # button_box.add_widget(self.button_pos1)
        button_box.add_widget(self.btn1)
        button_box.add_widget(self.btn2)
        button_box.add_widget(self.btn3)


        self.label = Label()
        Window.bind(mouse_pos=lambda w, p: setattr(self.label, 'text', str(p)))
        pos_box.add_widget(self.label)

        '''slider = Slider(orientation='vertical',min=0,max=100,value=0,value_track=True,value_track_color=[1,0,0,1],
                        on_value = str(Slider.value))'''

        #value= NumericProperty(str(int(slider.value)))
        #affichage = Label(text=str(value))

        button_box.add_widget(pos_box)
        superbox.add_widget(button_box)

        #superbox.add_widget(slider)
        #superbox.add_widget(affichage)

        return superbox


if __name__ == '__main__':
    LightApp().run()