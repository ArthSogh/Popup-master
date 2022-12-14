
"""TO USE WHEN WE WANT TO CREATE A COMMUNICATION BETWEEN LIGHTS AND THE APP"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from subprocess import Popen, PIPE


Builder.load_string("""
<MainScreen>:
    btn:btn
    btn2:btn2
    orientation: 'vertical'
    Label:
        id: msg
        text: "iSpheres Previous Application"
        font_size:32
        color: 1,0,0,1
        pos_hint: {"top":0.8}

    Button:
        id: btn
        size_hint: 1,0.2
        text: "Open Light's Screen"
        on_release:  root.btn_touch_up()
        
    Button: 
        id : btn2
        text: "Internal operation"
        size_hint: 1,0.2
        background_color: 0,1,1,1
        on_press: print('hello'),root.intern_modification()

""")


class MainScreen(BoxLayout):
    btn = ObjectProperty(None)

    '''Launching a complete new pycharm window by running 'moving_circle.py' separately'''
    @staticmethod
    def btn_touch_up():
        Popen(['python', 'moving_circle.py'], stdin=PIPE, stdout=PIPE)

    '''Some test to know if main application : iSpheres.py still work during the launch'''
    def intern_modification(self):
        self.btn2.text = "Changed"
        self.btn2.background_color = 1, 0, 1, 1


class TouchApp(App):
    import moving_circle

    def build(self):
        return MainScreen()

    def montre2(self):
        print('test')

if __name__ == "__main__":
    TouchApp().run()
