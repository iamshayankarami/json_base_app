import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

kivy.require("1.10.1")

class sing_in(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**wargs)
		self.cols = 2
		self.add_widget(Label(text="name:"))
		self.name = TextInput(multiline=False)
		self.add_widget(self.ip)
		
		self.add_widget(Label(text="username:"))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text="password:"))
		self.password = TextInput(multiline=False)
		self.add_widget(self.password)
		
		self.add_widget(Label(text="work:"))
		self.work = TextInput(multiline=False)
		self.add_widget(self.work)

		self.add_widget(Label(text="timeline:"))
		self.timeline = TextInput(multiline=False)
		self.add_widget(self.timeline)

		self.add_widget(Label(text="location:"))
		self.location = TextInput(multiline=False)
		self.add_widget(self.location)


class login_page(GridLayout):
	pass

class main_user_page(GridLayout):
	pass

class 
