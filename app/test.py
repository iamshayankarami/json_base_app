from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('test.kv')

class MainScreen(ScreenManager):
	pass
class login(Screen):
	pass
class Main(App):
	def build(self):
		return MainScreen(0)

if __name__ == '__main__':
	Main().run()
