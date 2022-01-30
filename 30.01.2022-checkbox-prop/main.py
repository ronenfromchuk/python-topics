import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

class DbGenWidget(Widget):
    option1 = ObjectProperty(None)
    option2 = ObjectProperty(None)
    option3 = ObjectProperty(None)

    # root.btn() in kv file
    def btn(self):
        pass
    def checkbox_click(self, instance, value):
        if value is True:
            print(f"Checkbox Checked {instance}")
        else:
            print(f"Checkbox Unchecked {instance}")
        print(self.option1.active)
        print(self.option2.active)
        print(self.option3.active)

class MyApp(App):   
    def build(self):
        return DbGenWidget()
    # app.btn() in kv file
    def btn(self):
        print('clicked...')        


Builder.load_file('my1.kv')

if __name__ == "__main__":
    MyApp().run()