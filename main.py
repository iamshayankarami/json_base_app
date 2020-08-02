from flask import Flask, request
import sqlite3 as sql

app = Flask(__name__)


def print_data(c,search):
	for row in c.execute(f"SELECT * FROM {search}"):
		return row

def check_mac_add(mac_add):
	mac_ad

@app.route('/', methods=["GET", "POST"])
def index():
	ip_add = request.remote_addr
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
			c.execute('SELECT name FROM sqlite_master WHERE type="table";')
			for names in c.fetchall():
				names = names[0]
				print([row for row in c.execute(f"SELECT * FROM {names}")])
			conn.commit()
	return "<form method='POST'><p>name: </p><input type='text' name='name' id='name'><br><p>work: </p><input type='text' name='work' id='work'<br><p>timeline: </p><input type='text' name='timeline' id='timeline'><br><input type='text' name='timerange' id='timerange'><br><input type='submit' value='Submit'></form> <p>{{data}}</p>"	
	conn.close()

if __name__ == '__main__':
	app.run(debug=True)
