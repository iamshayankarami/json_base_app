from flask import Flask, request
import sqlite3 as sql

app = Flask(__name__)


def print_pass_ips():
	return_data = []
	send = []
	with sql.connect('test1.db') as co:
		c = co.cursor()
		c.execute('SELECT name FROM sqlite_master WHERE type="table";')
		for name in c.fetchall():
			name = name[0]
			return_data.append([row for row in c.execute(f"SELECT * FROM {name}")])
	for data in return_data:
		data = data[0]
		send.append(data[1])
	return send

def _check_ip(ip, lisT):
	output = []
	for IP in lisT:
		if IP == ip:
			output.append(IP)
	if len(output) >= 1:
		print('old user')
	else:
		pass

@app.route('/', methods=["GET", "POST"])
def index():
	ip_add = request.remote_addr
	check_ip = print_pass_ips()
	_check_ip(ip_add, check_ip)
	if request.method == "POST":
		name = request.form["name"]
		work = request.form["work"]
		timeline = request.form["timeline"]
		timerange = request.form["timerange"]
		data = [(name, ip_add, work, timeline, timerange)]
		with sql.connect('test1.db') as conn:
			c = conn.cursor()
			c.execute(f'CREATE TABLE {name} (name, ip, work, timeline, timerange)')
			c.executemany(f"INSERT INTO {name} VALUES (?, ?, ?, ?, ?)", data)
			conn.commit()
	return "<form method='POST'><p>name: </p><input type='text' name='name' id='name'><br><p>work: </p><input type='text' name='work' id='work'<br><p>timeline: </p><input type='text' name='timeline' id='timeline'><br><input type='text' name='timerange' id='timerange'><br><input type='submit' value='Submit'></form> <p>{{data}}</p>"	
	conn.close()

if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)

