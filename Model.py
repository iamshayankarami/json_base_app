import time
import json
import os
import hashlib

json_file_name = 'data.json'

def get_time():
	return time.asctime()[11:19]

def today_date():
	return time.asctime()

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


def get_send_data(file_status=json_file_status()):
	if file_status == 'ture':
		send_data = {}
	else:
		with open(json_file_name, 'r') as read:
			send_data = json.load(read)
	return send_data

def json_singin(data):
	send_data = get_send_data()
	location = data[5].split('/')[0]
	geuss = [table for table in send_data if table == location]
	data_send_json = {}
	data_send_json[data[1]] = []
	data_send_json[data[1]].append({'name': data[0], 'username': data[1], 'password': data[2], 'timeline': data[3], 'work': data[4], 'location': data[5], 'ip': data[6]})
	data_send_json[data[1]].append({'name': data[0], 'username': data[1], 'timeline': data[3], 'work': data[4], 'location': data[5]})
	data_send_json[data[1]].append({'requests': []})
	data_send_json[data[1]].append({'send_requests': []})
	#data_send_json[data[1]].append({'user_activation': ['sing_in']})
	if geuss == []:
		send_data[location] = []
		send_data[location].append(data_send_json)
	else:
		send_data[geuss[0]].append(data_send_json)
	with open(json_file_name, 'w') as write:
		json.dump(send_data, write)

def get_time_range_of_user():
	pass

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
			for line in send_data[loc]:
				for name in line:
					append_data.append(line[name][1])
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
	with open(json_file_name, 'w') as Write:
		json.dump(send_data)



def sing_in():
	print('write your private information ["private key"]')
	name = input('Name: ')
	username = input('username: ')
	password = make_password_to_save(input('password: '))
	timeline = input('timeline: ')
	work = input('work: ')
	location = input('location: ')
	ip = '10:23:33:4d'
	all_money = 0
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
