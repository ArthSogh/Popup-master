from configparser import ConfigParser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

file = 'config_library.cfg'
config = ConfigParser()
config.read(file)

print(config.sections())
print(list(config['Step1']))
print(config['Step1']['time'])


class ConfigPage(GridLayout):
    def switch_callback(self, switchObject, switchValue):
        print(switchValue)

    def configrelays(self):
        for id in list(config['Step1']):
            self.switch_callback(self.c1)


class MyconfigApp(App):
    pass

if __name__ == '__main__':
    MyconfigApp().run()
