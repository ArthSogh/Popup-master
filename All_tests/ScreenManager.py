






""" Changing screens by 'screen manager'. No new windows will be opened, but the current screen will slide to the x one """







import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen


class Menu(Screen):
    pass

class P(Screen):
    pass

class PressureSlider(Screen):
    pass


class MyApp(App):
    def build(self):
        # Create the manager
        sm = ScreenManager()
        sm.add_widget(Menu(name="Ecran1"))
        sm.add_widget(P(name="Ecran2"))
        #sm.add_widget(PressureSlider@MDSlider(name="Ecran2"))
        #return Widgets()
        return sm


if __name__ == "__main__":
    MyApp().run()