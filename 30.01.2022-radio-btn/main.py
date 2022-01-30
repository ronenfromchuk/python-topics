import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, StringProperty

class DbGenWidget(Widget):

    slabel1 = StringProperty('On')
    slabel2 = StringProperty('Off')

    def switchstate1(self):
        # Switch radio button 1 on and process event trigger
        # Force 'down' state to avoid deselecting all radio buttons (Kivy thing)
        self.ids.rbutton1.state = 'down'
        # Update optional label values
        self.slabel1 = 'on'
        self.slabel2 = 'off'
        print(self.ids.rbutton1.state, self.ids.rbutton2.state)

    def switchstate2(self):
        # Switch radio button 2 on and process event trigger
        # Force 'down' state to avoid deselecting all radio buttons (Kivy thing)
        self.ids.rbutton2.state = 'down'
        # Update optional label values
        self.slabel1 = 'off'
        self.slabel2 = 'on'
        print(self.ids.rbutton1.state, self.ids.rbutton2.state)

def btn(self):
    pass

class MyApp(App):   
    def build(self):
        return DbGenWidget()
    # app.btn() in kv file
    def btn(self):
        print('clicked...')        


Builder.load_file('my1.kv')

if __name__ == "__main__":
    MyApp().run()