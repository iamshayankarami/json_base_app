import time
import json
import os
import hashlib

#TODO find userinfo by ip have to change to something else 

json_file_name = 'test1.json'

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
	location = data[5].split('/')[0]
	geuss = [table for table in send_data if table == location]
	data_send_json = {}
	data_send_json[data[1]] = []
	data_send_json[data[1]].append({'name': data[0], 'username': data[1], 'password': data[2], 'timeline': time_line_for_every_day(data[3]), 'work': data[4], 'location': data[5], 'ip': data[6]})
	data_send_json[data[1]].append({'name': data[0], 'username': data[1], 'timeline': time_line_for_every_day(data[3]), 'work': data[4], 'location': data[5]})
	data_send_json[data[1]].append({'requests': []})
	data_send_json[data[1]].append({'send_requests': []})
	data_send_json[data[1]].append({'user_activation': 'log-in'})
	#data_send_json[data[1]].append({'time_line': time_line_for_every_day(data[3].split('/'))})
	if geuss == []:
		send_data[location] = []
		send_data[location].append(data_send_json)
	else:
		send_data[geuss[0]].append(data_send_json)
	with open(json_file_name, 'w') as write:
		json.dump(send_data, write)

def get_time_range_of_user():
	pass

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

def add_request(send_user, user_name, request_thing, time_loc):
	send_data = get_send_data()
	return_data = {'request_from': user_name, 'request_send_time': time_loc, 'request_thing': request_thing, 'request_status': 'sended_request'}

	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if send_user == name:
					user[name][2]['requests'].append(return_data)

	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if send_user == name:
					user[name][3]['send_requests'].append({'request_to': send_user, 'request_send_time': time_loc, 'request_thing': request_thing, 'request_status': 'sended_request'})
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
					users[name][2]['requests'].append({'request_from': from_user, 'time': time_to})
				elif from_user == name:
					users[name][3]['send_requests'].append({'request_to': user, 'time': time_to})
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
	send_data=[i for i in time_send if i>int(time_line[0])-1 and i<int(time_line[1])+1]
	for data in send_data:
		show_data.append([f"{data}:{i}" for i in range(60) if i%int(time_line[2])==0])
	return show_data