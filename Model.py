import time
import sqlite3 as sql

def get_time():
	return time.asctime()[11:19]


def __check_num(Time):
	return Time[0:2]

def get_data_from_user():
	name = input('Name: ')
	work = input('Work: ')
	Time = __check_num(get_time())
	return [(name, work, Time)]

def send_to_database(data):
	with sql.connect('test.db') as conn:
		c = conn.cursor()
		c.execute(f'CREATE TABLE {data[0][0]} (name, work, time)')
		c.executemany(f"INSERT INTO {data[0][0]} VALUES(?, ?, ?)", data)
		conn.commit()

def print_all():
	with sql.connect('test.db') as conn:
		c = conn.cursor()
		c.execute('SELECT name FROM sqlite_master WHERE type="table";')
		for name in c.fetchall():
			for row in c.execute(f'SELECT * FROM {name[0]}'):
				print(row)

print_all()
