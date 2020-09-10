from flask import Flask, request, render_template, url_for, redirect, session
import os, time
from Model import make_password_to_save, json_singin, get_send_data, get_user_to, get_user_info_by_device_ip_add, show_all_users_poblic_data_in_user_location, LogOuT, change_ip_add, check_active, login_m, show_requests, send_request, time_line_for_every_day, send_Request

app = Flask(__name__)
app.secret_key = 'shayan-karami-secret-key-for-flask'


def get_time():
	return time.asctime()[11:19]

def __check_num(Time):
	return Time[0:2]


def find_file():
	for filename in os.listdir():
		data = filename.split('.')
		if len(data) >= 2:
			if data[1] == 'db': return data['name']+'.db'


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
		session['username']=username
		return redirect(url_for('index'))
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
				session['username']=username
				return redirect(url_for('index'))
			else:
				return 'wronge password'
	return '''<center>
	<form method='POST'>
		<p>username</p><input type='text', name='username'><br><p>password</p><input type='password' name='password'><br><input type='submit' name='submit' id='submit'>
	</form>
</center>
'''

@app.route('/', methods=["GET", "POST"])
def index():
	if 'username' in session:
		username = session['username']
		if get_user_to(username)[4]['user_activation'] == 'log-out':
			return redirect(url_for('login'))
		#print(check_active(username))
		user_poblic_info = get_user_to(username)[1]
		user_provate_info = get_user_to(username)[0]
		user_requests = get_user_to(username)[2]
		user_send_requests = get_user_to(username)[3]
		return f'''<p>main page of {user_provate_info['name']}</p><a href="{url_for('SHOW_ALL')}">show_all</a><br><a href={url_for('logout')}>log out</a><br><b>you have {len(user_requests['requests'])} requests </b><b>{show_requests(username)}</b>'''
	return render_template('welcome.php')


@app.route('/show_all')
def SHOW_ALL():
	#ip_add = request.remote_addr
	if 'username' in session:
		username=session['username']
		user_data=get_user_to(username)
		show_data = show_all_users_poblic_data_in_user_location(user_data[1]['location'])
		return ''.join([f'''<a href={url_for('show_user', show_username=users[1]['username'])}>{users[1]['username']} </a><b>{users[1]['work']} </b><br><br>''' for users in show_data if users[1]['username'] != username])
	return redirect(url_for('index'))


@app.route('/show_data_of', methods=['POST', 'GET'])
def show_user():
	if 'username' in session:
		show_username = request.args.get('show_username', None)
		username = session['username']
		status = send_Request(username, show_username)
		timelines = status.check_time_line()
		if request.method == 'POST':
			select = request.form.get('select_form_time')
			status.chose_time_to_send(select)
			status.send_request_to_user_in_command_line()
			return redirect(url_for('show_my_send_requests'))
		return render_template('show_all.html', time_line=timelines)
	return redirect(url_for('index'))

@app.route('/show_my_send_requests')
def show_my_send_requests():
	if 'username' in session:
		all_of_my_request = get_user_to(session['username'])[3]['send_requests']
		send_text = []
		for re in all_of_my_request:
			send_text.append(f"{re['request_to']} {re['time']} {re['request_activ']}")
		return render_template('show_my_sends_requets.html', data=send_text)
	return redirect(url_for('index'))

@app.route('/logout')
def logout():
	#ip_add = request.remote_addr
	if 'username' in session:
		LogOuT(session['username'])
		session.pop('username', None)
		return redirect(url_for('index'))
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
