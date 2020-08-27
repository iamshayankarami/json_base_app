from flask import Flask, request, render_template, url_for, redirect
import os, time
from Model import make_password_to_save, json_singin, get_send_data, get_user_to, get_user_info_by_device_ip_add, show_all_users_poblic_data_in_user_location, LogOuT, change_ip_add, check_active, login_m, show_requests, send_request, time_line_for_every_day

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


@app.route('/singin', methods=["GET", "POST"])
def singin():
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
		return redirect(url_for('index', username=username))
	#return render_template("singin.html")
	return '''<center><form method='POST'><p>name</p><input type='text' name='name'><br><p>username</p><input type='text', name='username'><br><p>password</p><input type='password' name='password'><br><p>work</p><input type='text' name='work'><br><p>timeline</p><input type='text' name='timeline'><br><p>location</p><input type='text' name='location'><br><input type='submit' name='submit' id='submit'></form></center>'''


@app.route('/login', methods=["GET", "POST"])
def login():
	ip_add = request.remote_addr
	if request.method == "POST":
		username = request.form["username"]
		password = make_password_to_save(request.form["password"])
		if get_user_to(username)[0] == []:
			return 'username not founded'
		else:
			if password == get_user_to(username)[0]['password']:
				#change_ip_add(username, ip_add)
				login_m(username)
				return redirect(url_for('index', username=username))
			else:
				return 'wronge password'
	return render_template('login.html')

@app.route('/', methods=["GET", "POST"])
def index():
	#ip_add = request.remote_addr
	#ip_add = '10:23:33:4d' #just for testing
	#user_username = get_user_info_by_device_ip_add(ip_add)
	username = request.args.get('username', None)
	if get_user_to(username)[4]['user_activation'] == 'log-out':
		return redirect(url_for('login'))
	#print(check_active(username))
	#user_poblic_info = get_user_to(username)[1]
	user_provate_info = get_user_to(username)[0]
	user_requests = get_user_to(username)[2]
	#user_send_requests = get_user_to(username)[3]
	return f'''<p>main page of {user_provate_info['name']}</p><a href="{url_for('SHOW_ALL', username=username)}">show_all</a><br><a href={url_for('logout', username=username)}>log out</a><br><b>you have {len(user_requests['requests'])} requests </b><b>{show_requests(username)}</b>'''


@app.route('/show_all')
def SHOW_ALL():
	#ip_add = request.remote_addr
	user_username = request.args.get('username', None)
	user_data=get_user_to(user_username)
	show_data = show_all_users_poblic_data_in_user_location(user_data[0]['location'])
	return ''.join([f'''<a href={url_for('show_user', show_username=users[0]['username'], my_username=user_username)}>{users[0]['username']} </a><b>{users[0]['work']} </b><br><br>''' for users in show_data if users != users[0]['username'] != user_username])

@app.route('/show_data_of', methods=['POST', 'GET'])
def show_user():
	show_username = request.args.get('show_username', None)
	my_username = request.args.get('my_username', None)
	sho = ''.join([f'''<option>{times[0]} to {times[1]}</button> <br><br>''' for times in get_user_to(show_username)[1]['timeline']])
	return f'<select name="times">{sho}</select>'

@app.route('/send_request', methods=['POST', 'GET'])
def send_Request():
	my_username = request.args.get('my_username', None)
	send_username = request.args.get('send_username', None)
	if request.method == 'POST':
		Time = request.form["Time"]
		print({'send_to': send_username, 'from_you': my_username, 'time': Time})
		send_request(send_username, my_username, Time)
	return f"<form method='POST'><p>Time: </p><input type='text' name='Time'><input type='submit' name='submit' id='submit'></form>"

@app.route('/logout')
def logout():
	#ip_add = request.remote_addr
	LogOuT(request.args.get('username', None))
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)
