import kivy, json, os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require("1.10.1")

class singin(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols, self.return_data = 2, {}
		
		self.add_widget(Label(text='Name: '))
		self.name = TextInput(multiline=False)
		self.return_data['name']=self.name
		self.add_widget(self.name)

		self.add_widget(Label(text='Username: '))
		self.username = TextInput(multiline=False)
		self.return_data['username']=self.username
		self.add_widget(self.username)

		self.add_widget(Label(text='Password: '))
		self.password = TextInput(password=True, multiline=False)
		self.return_data['passeord']=self.password
		self.add_widget(self.password)

		self.add_widget(Label(text='Work: '))
		self.work = TextInput(multiline=False)
		self.return_data['work']=self.work
		self.add_widget(self.work)

		self.add_widget(Label(text='Timeline: '))
		self.timeline = TextInput(multiline=False)
		self.return_data['timeline']=self.timeline
		self.add_widget(self.timeline)

		self.add_widget(Label(text='Location: '))
		self.location = TextInput(multiline=False)
		self.return_data['location']=self.location
		self.add_widget(self.timeline)

class login(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class mainPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class Main(App):
	def build(self):
		pass

if __name__ == '__main__':
	main_app = Main()
	main_app.run()
