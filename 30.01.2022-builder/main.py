import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

class MyWidget(Widget):
    # root.btn() in kv file
    def btn(self):
        print('clicked...')
   
class MyApp(App):
    def build(self):
        return MyWidget()
    # app.btn() in kv file
    def btn(self):
        print('clicked...')        


Builder.load_file('my1.kv')

if __name__ == "__main__":
    MyApp().run()