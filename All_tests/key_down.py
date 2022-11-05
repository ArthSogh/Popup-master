from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty,StringProperty


class Keydown_screen(BoxLayout):
    pass

class KeyDownApp(App):

    key_action_text = StringProperty('Touch the keyboard')

    def build(self):
        Window.bind(on_key_down=self.key_action)
        return Keydown_screen()

    def key_action(self, *args):
        print("got a key event: %s" % list(args)[3])
        self.key_action_text = str(list(args)[3])
        print(self.key_action_text)
        self.close_on_key_touch_one()


    def close_on_key_touch_one(self):
        if self.key_action_text == 'k':
            print('passed')
            Window.close()
            self.close_on_key_touch_two()


    def close_on_key_touch_two(self):
        print('here we are')
        while True:
            if self.key_action_text != 's':
                print('almost')
            else:
                break

if __name__ == '__main__':
    KeyDownApp().run()