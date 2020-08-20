from flask import Flask, request, render_template, url_for, redirect
import os, time
from Model import make_password_to_save, json_singin, get_send_data, get_user_to, get_user_info_by_device_ip_add, show_all_users_poblic_data_in_user_location, LogOut

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
	ip_add = request.remote_addr
	#ip_add = '10:23:33:4d' #just for testing
	user_username = get_user_info_by_device_ip_add(ip_add)

	user_poblic_info = get_user_to(user_username)[1]
	user_provate_info = get_user_to(user_username)[0]
	user_requests = get_user_to(user_username)[2]
	user_send_requests = get_user_to(user_username)[3]
	return f'''<p>main page of {user_provate_info['name']}</p><a href="/show_all">show_all</a><br><a href="/logout">log out</a><b>{os.environ['USER']}</b>'''


@app.route('/show_all')
def SHOW_ALL():
	ip_add = request.remote_addr
	user_username = get_user_info_by_device_ip_add(ip_add)
	user_data=get_user_to(user_username)
	show_data = show_all_users_poblic_data_in_user_location(user_data[0]['location'])
	return ''.join([f"<b>{users[0]['name']} </b><b>{users[0]['work']} </b><b>{users[0]['timeline']} </b><b>{users[2]['requests']}</b><br>" for users in show_data])
	#return render_template('show_all.html', data=send)

@app.route('/logout')
def logout():
	ip_add = request.remote_addr
	user_username = get_user_info_by_device_ip_add(ip_add)
	LogOut(user_username)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)
