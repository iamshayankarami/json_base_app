import time
import json
import os


def get_time():
	return time.asctime()[11:19]

def today_date():
	return time.asctime()

def __check_num(Time):
	return Time[0:2]

def make_password_to_save(password):
	return hashlib.sha256(password.encode()).hexdigest()

def get_data_from_user():
	name = input('Name: ')
	work = input('Work: ')
	Time = __check_num(get_time())
	data = name, work, Time
	return data

#lets go to json, I'm the best programmer in the world, I LOVE CODING

def get_json(data):
	with open('data.json', 'r') as readfile:
		send_data = json.load(readfile)
	gusse_table = [table_name for table_name in send_data if table_name == data[0]]
	if gusse_table == []:
		send_data[data[0]] = []
		send_data[data[0]].append({'name': data[1], 'work': data[2]})
		with open('data.json', 'w') as jfile:
			json.dump(send_data, jfile)
	else:
		send_data[gusse_table[0]].append({'name': data[1], 'work': data[2]})

def send_request(send_user, name, time_range):
	with open('data.json', 'r') as read:
		send_data = json.load(read)
	gusse_table = [table_name for table_name in send_data if table_name == send_user]
	if gusse_table != []:
		send_data[gusse_table[0]].append({'request_user': name, 'time_range': time_range})
	else:
		print('user not founded')
		


def main():
	user = get_data_from_user()
	today = today_date()
	to = ''
	to = to+today[:10]+today[19:] 
	data = (to, user[0], user[1], user[2])
	get_json(data)

if __name__ == '__main__':
	main()
