
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class login(GridLayout):
    def __init__(self):
        super().__init__()
        self.cols=2
        self.add_widget(Label(text="Author name:"))
        self.authorname = TextInput(multiline=False)
        self.add_widget(self.authorname)
        self.add_widget(Label(text="Music name:"))
        self.musicname = TextInput(multiline=False)
        self.add_widget(self.musicname)

class MyApp(App):
    def build(self):
        return login()
if __name__ == '__main__':

    MyApp().run()
