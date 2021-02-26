import json
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

dictionary_data = json.load(open("dictionary_data.json"))
Builder.load_file('design.kv')

class AppLayout(Widget):
    def dictionary_search(self):
        """Take a user input and search for it in a dictionary."""

        word = self.ids.search_word.text
        display = self.ids.display
        try:
            display.text = '\n'.join(dictionary_data[word.lower()])
        except:
            display.text = "Please check the spelling on your word."


class DictionaryApp(App):
    def build(self):
        return AppLayout()


if __name__ == "__main__":
    DictionaryApp().run()
