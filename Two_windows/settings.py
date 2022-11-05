from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_string("""
Screen:
    Label:
        text: 'Setting Screen'
        font_size: 23
        pos_hint: {"top":1.2}
            
    BoxLayout:
        
        orientation: 'horizontal'
        
        Button:
            text: 'Exit'
            size_hint: 0.2,0.2
            on_release: app.stop()
        
        Button:
            text: 'Button2'
            size_hint: 0.2,0.2
            on_release: app.stop()
        Button:
            text: 'Button3'
            size_hint: 0.2,0.2            
            on_release: app.stop()
""")

class SettingScreen(App):
    def build(self):
        return kv

if __name__ == "__main__":
    SettingScreen().run()