import time
import json
import os
import hashlib


json_file_name = '/home/pi/json_files/test2.json'

def get_time():
	return time.asctime()[11:19]

def today_date():
	re = f"{time.asctime()[:11]}{time.asctime()[20:]}"
	return re

def __check_num(Time):
	return Time[0:2]

def make_password_to_save(password):
	return hashlib.sha256(password.encode()).hexdigest()

def json_file_status():
	with open(json_file_name, 'r') as Read:
		if Read.read() == '':
			return 'true'
		else:
			return 'false'


def get_send_data():
	with open(json_file_name, 'r') as ReaD:
		send_data = json.load(ReaD)
	return send_data


def json_singin(data):
	send_data = get_send_data()
	location = data['location'].split('/')[0]
	geuss = [table for table in send_data if table == location]
	data_send_json = {}
	data_send_json[data['username']] = []
	data_send_json[data['username']].append({'name': data['name'], 'username': data['username'], 'password': data['password'], 'timeline': time_line_for_every_day(data['timeline']), 'work': data['work'], 'location': data['location']})
	data_send_json[data['username']].append({'name': data['name'], 'username': data['username'], 'timeline': time_line_for_every_day(data['timeline']), 'work': data['work'], 'location': data['location']})
	data_send_json[data['username']].append({'requests': []})
	data_send_json[data['username']].append({'send_requests': []})
	data_send_json[data['username']].append({'user_activation': 'log-in'})
	#data_send_json[data['username]].append({'time_line': time_line_for_every_day(data['timeline'].split('/'))})
	if geuss == []:
		send_data[location] = []
		send_data[location].append(data_send_json)
	else:
		send_data[geuss[0]].append(data_send_json)
	with open(json_file_name, 'w') as write:
		json.dump(send_data, write)

def Longin(push_data):
	if get_user_to(push_data['username'])[0] == []:
		print('user not found')
	else:
		if push_data['password'] == get_user_to(push_data['username'])[0]['password']:
			login_m(push_data['username'])
		else:
			print('wronge password')

def change_ip_add(username, ip_add):
	send_data = get_send_data()
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if name == username:
					if user[name][0]['ip'] != ip_add:
						user[name][0]['ip'] = ip_add
	with open(json_file_name, 'w') as W:
		json.dump(send_data, W)



def get_user_info_by_device_ip_add(ip_add):
	send_data = get_send_data()
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if user[name][0]['ip'] == ip_add: return name


def show_all_users_poblic_data_in_user_location(user_location):
	append_data = []
	send_data = get_send_data()
	for loc in send_data:
		if user_location == loc:
			for user in send_data[loc]:
				for name in user:
					append_data.append(user[name])
	return append_data

def get_user_to(usern):
	send_data = get_send_data()
	for citis in send_data:
		for ur in send_data[citis]:
			for users in ur:
				if users == usern:
					return ur[users]

def delete_user(username):
	send_data = get_send_data()
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if username == name:
					send_data[citi].remove(user)

def add_request(send_user, user_name, time_loc):
	send_data = get_send_data()
	return_data = {'request_from': user_name, 'time': time_loc, 'request_status': 'sended_request'}

	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if send_user == name:
					user[name][2]['requests'].append(return_data)

	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if send_user == name:
					user[name][3]['send_requests'].append({'request_to': send_user, 'time': time_loc, 'request_status': 'sended_request'})
	with open(json_file_name, 'w') as write_file:
		json.dump(send_data, write_file)

def LogOuT(username):
	send_data = get_send_data()
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if username == name:
					user[name][4]['user_activation'] = 'log-out'
	with open(json_file_name, 'w') as W:
		json.dump(send_data, W)

def login_active(username):
	send_data = get_send_data()
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if name == username:
					user[name][4]['user_activation'] = 'log-in'
	with open(json_file_name, 'w') as write_file:
		json.dump(send_data, write_file)

def login_m(username):
	send_data = get_send_data()
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if username == name:
					user[name][4]['user_activation'] = 'log-in'
	with open(json_file_name, 'w') as W:
		json.dump(send_data, W)

def check_active(username):
	return get_user_to(username)[4]

def show_requests(username):
	if len(get_user_to(username)[2]['requests'])>=1:
		return get_user_to(username)[2]['requests']
	else:
		return ''

def check_user_activation(username):
	return get_user_to(username)[4]

def send_request(user, from_user, time_to):
	send_data = get_send_data()
	for citi in send_data:
		for users in send_data[citi]:
			for name in users:
				if user == name:
					users[name][2]['requests'].append({'request_from': from_user, 'time': time_to, 'request_activ': 'request_sended'})
				elif from_user == name:
					users[name][3]['send_requests'].append({'request_to': user, 'time': time_to, 'request_activ': 'request_sended'})
	with open(json_file_name, 'w') as write_file:
		json.dump(send_data, write_file)


def sing_in():
	print('write your private information ["private key"]')
	name = input('Name: ')
	username = input('username: ')
	password = make_password_to_save(input('password: '))
	timeline = input('timeline: ')
	work = input('work: ')
	location = input('location: ')
	ip = '10:23:33:4d'
	private_data = (name, username, password, timeline, work, location, ip)
	return private_data

def login():
	print('login')
	username = input('username: ')
	password = make_password_to_save(input('password: '))
	user_private_info = get_user_to(username)[0]
	if password == user_private_info['password']:
		print(f'welcome {user_private_info["name"]}')
		return get_user_to(username)[1]
	else:
		print('wronge password')

def time_line_for_every_day(time_line):
	show_data=[]
	time_line = time_line.split('/')
	time_send=[j for j in range(24)]
	send_data=[i for i in time_send if i>int(time_line[0])-1 and i<int(time_line[1])]
	for times in send_data:
		for i in range(60):
			if i%int(time_line[2]) == 0:
				if i+int(time_line[2])==60: show_data.append(f"{times}:{i} {times+1}:{0}")
				else: show_data.append(f"{times}:{i} {times}:{i+int(time_line[2])}")
	return show_data

class send_Request:
	def __init__(self, user_username, send_user_username):
		self.send_user_username = send_user_username
		self.user_username = user_username
	def check_time_line(self):
		self.times = get_user_to(self.send_user_username)[2]['requests']
		self.times = [t['time'] for t in self.times]
		self.times_from_timeline = get_user_to(self.send_user_username)[1]['timeline']
		if self.times == []: self.times_from_timeline
		else:
			#self.Time_line = [[time_line for timeshits in self.times if timeshits != time_line] for time_line in get_user_to(self.send_user_username)[1]['timeline']]
			self.check_times=[]
			for time_line in self.times_from_timeline:
				for line_time in self.times:
					if time_line == line_time:
						self.check_times.append(time_line)
			for time_lines in self.check_times:
				self.times_from_timeline.remove(time_lines)
				
		return self.times_from_timeline

	def chose_time_to_send(self, chose_file):
		self.chose_file = chose_file
		for times in self.times_from_timeline:
			if self.chose_file == times:
				print(f"\033[97m[INFO]\033[00m: time chosed {self.chose_file} is valibel now do you want to rejester? ")
				print(f'\033[97m[INFO]: \033[00m OK')
				return self.chose_file

	def send_request_to_user_in_command_line(self):
		send_request(self.send_user_username, self.user_username, self.chose_file)
		print(f"\033[97m[INFO]\033[00m: {self.chose_file} is sended to {self.send_user_username}")

def change_requets_act(username, time_line, change_to):
	send_data = get_send_data()
	for citi in send_data:
		for name in send_data[citi]:
			if name==username:
				for times in get_user_to(name)[3]['send_requests']:
					if times['time'] == time_line:
						show_user = times['request_status']
						times['request_arc'] = change_to
			elif name==show_user:
				for times in get_user_to(name)[2]['requests']:
					if times['time']==time_line:
						times['request_status'] = change_to
	with open(json_file_name, 'w') as Write_file:
		json.dump(send_data)
