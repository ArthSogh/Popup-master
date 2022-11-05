from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

class Constructor_Button(Screen):
    pass

class Constructor_Light(GridLayout):
    pass

class ScreenApp(App):
    def build(self):
        return Constructor_Button()
    def other(self):
        print('passed')

        return Constructor_Light()


if __name__ == "__main__":
    ScreenApp().run()