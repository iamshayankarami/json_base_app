from flask import Flask, request, render_template, url_for, redirect
import os, time
from Model import make_password_to_save, json_singin, get_send_data, get_user_to, get_user_info_by_device_ip_add

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


@app.route('/singin', methods=["GET", "POST"])
def singin():
	global user_username
	ip_add = request.remote_addr
	if request.method == 'POST':
		name = request.form["name"]
		work = request.form["work"]
		password = make_password_to_save(request.form["password"])
		username = request.form["username"]
		timeline = request.form["timeline"]
		location = request.form["location"]
		push_data = (name, username, password, timeline, work, location, ip_add)
		json_singin(push_data)
		user_username = username
		return redirect(url_for('index'))
	#return render_template("singin.html")
	return '''<center><form method='POST'><p>name</p><input type='text' name='name'><br><p>username</p><input type='text', name='username'><br><p>password</p><input type='password' name='password'><br><p>work</p><input type='text' name='work'><br><p>timeline</p><input type='text' name='timeline'><br><p>location</p><input type='text' name='location'><br><input type='submit' name='submit' id='submit'></form></center>'''


@app.route('/login', methods=["GET", "POST"])
def login():
	global user_username
	ip_add = request.remote_addr
	if request.method == "POST":
		username = request.form["username"]
		password = make_password_to_save(request.form["password"])
		if get_user_to(username)[0] == []:
			return 'username not founded'
		else:
			user_p_info = get_user_to(username)[0]
			if password == user_p_info['password']:
				user_username = username
				return redirect(url_for('Send_request'))
			else:
				return 'wronge password'
	return render_template('login.html')

@app.route('/send_request', methods=["GET", "POST"])
def Send_request():
	global user_username
	ip_add = request.remote_addr
	print(get_user_to(user_username))
	if request.method == "POST":
		send_to = request.form["send_to"]
		number = request.form["number"]
		timel = request.form["timel"]
	#add_request(send_to, number, timel)
	return f'<p>welcome to send page {user_username} </p>'

@app.route('/', methods=["GET", "POST"])
def index():
	#ip_add = request.remote_addr
	ip_add = '10:23:33:4d' #just for testing
	user_username = get_user_info_by_device_ip_add(ip_add)

	user_poblic_info = get_user_to(user_username)[1]
	user_provate_info = get_user_to(user_username)[0]
	user_requests = get_user_to(user_username)[2]
	user_send_requests = get_user_to(user_username)[3]
	print(user_poblic_info)
	return f'''<p>main page of {user_provate_info['work']}</p>'''

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
	app.run(debug=True)
