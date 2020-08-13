import time
import json
import os
from flask import Flask, request, render_template
import hashlib
app = Flask(__name__)

def get_time():
	return time.asctime()[11:19]

def today_date():
	return time.asctime()

def __check_num(Time):
	return Time[0:2]

def make_password_to_save(password):
	return hashlib.sha256(password.encode()).hexdigest()

def get_send_data():
	with open('all_data.json', 'r') as read:
		send_data = json.load(read)
	return send_data

def json_singin(data):
	send_data = get_send_data()
	location = data[5].split('/')[0]
	geuss = [table for table in send_data if table == location]
	data_send_json = {}
	data_send_json[data[1]] = []
	data_send_json[data[1]].append({'name': data[0], 'username': data[1], 'password': data[2], 'timeline': data[3], 'work': data[4], 'location': data[5], 'ip': data[6], 'all_money': data[7]})
	data_send_json[data[1]].append({'name': data[0], 'username': data[1], 'timeline': data[3], 'work': data[4], 'location': data[5]})
	data_send_json[data[1]].append({'requests': []})
	if geuss == []:
		send_data[location] = []
		send_data[location].append(data_send_json)
	else:
		send_data[geuss[0]].append(data_send_json)
	with open('all_data.json', 'w') as write:
		json.dump(send_data, write)

def get_time_range_of_user():
	pass

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


def add_request(send_user, my_data, time_loc):
	user_data = get_user_to(send_user)
	user_data.append(
	

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
	private_data = (name, username, password, timeline, work, location, ip, all_money)
	publice_data = (username, timeline, work, location)
	return private_data, publice_data

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

print('are you a new user? [Y, N]')
g = input()
if g == 'Y' or g=='y' or g=='':
	data = sing_in()[0]
	json_singin(data)
elif g=='N' or g=='n':
	my_data = login()
	send_to = input('buy from: ')
	add_request(send_to, my_data, '7')		
