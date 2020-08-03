from flask import Flask, request
import sqlite3 as sql
import os


app = Flask(__name__)

def find_file():
	for filename in os.listdir():
		data = filename.split('.')
		if len(data) >= 2:
			if data[1] == 'db': return data[0]+'.db'

class show_all:
	def __init__(self, ip):
		self.ip = ip

	def print_pass_ips(self):
		self.return_data = []
		self.send = []
		with sql.connect(find_file()) as co:
			c = co.cursor()
			c.execute('SELECT name FROM sqlite_master WHERE type="table";')
			for name in c.fetchall():
				name = name[0]
				self.return_data.append([row for row in c.execute(f"SELECT * FROM {name}")])
		for data in self.return_data:
			data = data[0]
			self.send.append(data)
		return self.send

	def _check_ip(self):
		self.output = []
		self.user_data = []
		for IP in self.send:
			IPS = IP[1]
			if IPS == self.ip:
				self.output.append(IP)
				self.user_data.append(IP)
		if len(self.output) >= 1:
			return 'old user'
		else:
			pass
	def print_user_data(self):
		return self.user_data[len(self.user_data)-1]

@app.route('/', methods=["GET", "POST"])
def index():
	ip_add = request.remote_addr
	s = show_all(ip_add)
	check_ip = s.print_pass_ips()
	check = s._check_ip()
	if request.method == "POST":
		name = request.form["name"]
		work = request.form["work"]
		timeline = request.form["timeline"]
		timerange = request.form["timerange"]
		data = [(name, ip_add, work, timeline, timerange)]
		with sql.connect(find_file()) as conn:
			c = conn.cursor()
			c.execute(f'CREATE TABLE {name} (name, ip, work, timeline, timerange)')
			c.executemany(f"INSERT INTO {name} VALUES (?, ?, ?, ?, ?)", data)
			conn.commit()
	if check == 'old user':
		text = ''
		for edj in s.print_user_data():
			text = text+' '+edj
		return text
	else:
		return "<form method='POST'><p>name: </p><input type='text' name='name' id='name'><br><p>work: </p><input type='text' name='work' id='work'<br><p>timeline: </p><input type='text' name='timeline' id='timeline'><br><input type='text' name='timerange' id='timerange'><br><input type='submit' value='Submit'></form> <p>{{data}}</p>"	
if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)

