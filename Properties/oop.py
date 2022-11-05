from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty,StringProperty,NumericProperty,BoundedNumericProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout


class Mygrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name: ", self.name.text, "Email:", self.email.text)
        self.name.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return Mygrid()

    def btn(self):
        print("Name2: ", self.name.text, "Email2:", self.email.text)
        self.name.text = ""
        self.email.text = ""

if __name__ == "__main__":
    MyApp().run()