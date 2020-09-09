import kivy, json, os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

def check_the_inputs(input_data):
	for parts in input_data:
		if input_data[parts] == '':
			return "ERROR"
		elif parts == 'timeline':
			if len(input_data[parts].split('/')) != 3:
				return "ERROR"

class singin(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		
		self.add_widget(Label(text='Name: '))
		self.name = TextInput(multiline=False)
		self.add_widget(self.name)

		self.add_widget(Label(text='Username: '))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text='Password: '))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)

		self.add_widget(Label(text='Work: '))
		self.work = TextInput(multiline=False)
		self.add_widget(self.work)

		self.add_widget(Label(text='Timeline: '))
		self.timeline = TextInput(multiline=False)
		self.add_widget(self.timeline)

		self.add_widget(Label(text='Location: '))
		self.location = TextInput(multiline=False)
		self.add_widget(self.location)

		self.Sing_in = Button(text="singin")
		self.Sing_in.bind(on_press=self.sing_in)
		self.add_widget(Label())
		self.add_widget(self.Sing_in)

	def sing_in(self, instance):
		self.return_data={'name': self.name.text, 'username': self.username.text, 'password': self.password.text, 'work': self.work.text, 'timeline': self.timeline.text, 'location': self.location.text}
		push_data=self.return_data
		if check_the_inputs(push_data) == None:
			print(push_data)
		else: print(check_the_inputs(push_data))

class login(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols=1
		
		self.add_widget(Label(text="username: "))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text="password"))
		self.password = TextInput(multiline=False, password=True)
		self.add_widget(self.password)

		self.logiN = Button(text="Login")
		self.logiN.bind(on_press=self.Login)
		self.add_widget(Label())
		self.add_widget(self.logiN)

	def Login(self, instance):
		self.push_data={'password': self.password.text}
		print(self.push_data)

class mainPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class Main(App):
	def build(self):
		return login()

if __name__ == '__main__':
	Main().run()
