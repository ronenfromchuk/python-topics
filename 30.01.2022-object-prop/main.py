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
    airline_companies = ObjectProperty(None)
    customers = ObjectProperty(None)
    administrators = ObjectProperty(None)
    flights_per_company = ObjectProperty(None)
    tickets_per_customer = ObjectProperty(None)
    countries = ObjectProperty(None)

    # root.btn() in kv file
    def btn(self):
        print("Airline Companies:", self.airline_companies.text,
            "Customers:", self.customers.text,
            "Administrators:", self.administrators.text,
            "Flights Per Company:", self.flights_per_company.text,
            "Tickets Per Customer:", self.tickets_per_customer.text,
            "Countries:", self.countries.text)
   
class MyApp(App):   
    def build(self):
        return DbGenWidget()
    # app.btn() in kv file
    def btn(self):
        print('clicked...')        


Builder.load_file('my1.kv')

if __name__ == "__main__":
    MyApp().run()