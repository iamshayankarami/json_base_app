import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from Model import make_password_to_save, get_user_to, get_user_info_by_device_ip_add

kivy.require("1.10.1")

class sing_in(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 6
		self.add_widget(Label(text="name:"))
		self.name = TextInput(multiline=False)
		self.add_widget(self.name)
		
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
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 2

		self.add_widget(Label(text="username:"))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text="password:"))
		self.password = TextInput(multiline=False)
		self.add_widget(self.password)

	def join_button(self, instance):
		username = self.username.text
		password = make_password_to_save(self.password.text)
		user_p_info = get_user_to(username)[0]
		if user_p_info == '':
			print('no username founded')
		else:
			if user_p_info['password'] == password:
				print('coming in')
			else:
				print('wronge password')

class user_panel_page(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		pass

class MainApp(App):
	def build(self):
		return sing_in()

if __name__ == '__main__':
	MainApp.run()