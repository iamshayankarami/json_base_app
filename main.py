from flask import Flask, request, render_template
import sqlite3 as sql
import os, time

app = Flask(__name__)


def get_time():
	return time.asctime()[11:19]

def __check_num(Time):
	return Time[0:2]


def find_file():
	for filename in os.listdir():
		data = filename.split('.')
		if len(data) >= 2:
			if data[1] == 'db': return data[0]+'.db'

def get_database_datas():
	send = []
	with sql.connect(find_file()) as conn:
		c = conn.cursor()
		c.execute('SELECT name FROM sqlite_master WHERE type="table";')
		for name in c.fetchall():
			for row in c.execute(f"SELECT * FROM {name[0]}"):
				send.append(row)
	return send


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
		TIME = __check_num(get_time())
		data = [(name, ip_add, work, TIME)]
		with sql.connect(find_file()) as conn:
			c = conn.cursor()
			c.execute(f'CREATE TABLE {name} (name, ip, work, time)')
			c.executemany(f"INSERT INTO {name} VALUES (?, ?, ?, ?)", data)
			conn.commit()
	if check == 'old user':
		text = ''
		for edj in s.print_user_data():
			text = text+' '+edj
		return text
	else:
		return render_template('index.html', data=ip_add)
@app.route('/new_table', methods=['POST', 'GET'])
def new_tables():
	ip_add = request.remote_addr
	s = show_all(ip_add)
	check_ip = s.print_pass_ips()
	check = s._check_ip()
	if check == 'old user':
		text = ''
		for edj in s.print_user_data():
			text = text+' '+edj
		name = text.split(' ')[1]
		work = text.split(' ')[3]
	if request.method == "POST":
		time_line = request.form["time_L"]
		time_range = request.form["time_R"]
		data = [(name, ip_add, work, time_line, time_range)]
		with sql.connect(find_file()) as conn:
			c = conn.cursor()
			c.executemany(f"INSERT INTO {name} VALUES (?, ?, ?, ?, ?)", data)
			conn.commit()
	return "<form method='POST'><input type='text' id='time_L' name='time_L'><input type='text' id='time_R', name='time_R'> <input type='submit' value='Submit'></form>"

@app.route('/show_all')
def SHOW_ALL():
	send=''
	for data in get_database_datas():
		text = ''
		for line in data:
			text = text+' '+line
		send = send+'\n'+text
	return send
	#return render_template('show_all.html', data=send)

if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)
