import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('design.kv')

class AppLayout(Widget):
    pass

class DictionaryApp(App):
    def build(self):
        return AppLayout()


if __name__ == "__main__":
    DictionaryApp().run()