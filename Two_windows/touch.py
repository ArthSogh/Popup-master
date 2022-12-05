

"""TO USE WHEN WE WANT TO CREATE A COMMUNICATION BETWEEN LIGHTS AND THE APP"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from subprocess import Popen, PIPE

Builder.load_string("""
<Screen>:
    btn:btn
    orientation: 'vertical'
    Label:
        id: msg
        text: "iSpheres Previous Application"
        font_size:32
        color: 1,0,0,1
        pos_hint: {"top":0.8}

    Button:
        id: btn
        size_hint: 0.2,0.2
        text: "Touch Me ~ Lights"
        on_release:  root.btn_touch_up()

""")


class Screen(BoxLayout):
    btn = ObjectProperty(None)

    def btn_touch_up(self):
        print("Touch Up ")
        process = Popen(['python', 'settings.py'], stdin=PIPE, stdout=PIPE)
        print("Passed ")


class TouchApp(App):
    def build(self):
        return Screen()


if __name__ == "__main__":
    TouchApp().run()