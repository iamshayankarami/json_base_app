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

def get_data_from_user():
	name = input('Name: ')
	work = input('Work: ')
	Time = __check_num(get_time())
	data = name, work, Time
	return data

#lets go to json, I'm the best programmer in the world, I LOVE CODING
def singin_json(data):
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

def json_singin(data):
	with open('all_data.json', 'r') as read:
		send_data = json.load(read)
	location = data[5].split('/')[0]
	send_data[location] = {}
	send_data[location][data[1]] = {}
	send_data[location][data[1]]['private'] = {'name': data[0], 'username': data[1], 'password': data[2], 'timeline': data[3], 'work': data[4], 'location': data[5], 'ip': data[6], 'all_money': data[7]}
	send_data[location][data[1]]['poblic'] = {'name': data[0], 'username': data[1], 'timeline': data[3], 'work': data[4], 'location': data[5]}

	with open('all_data.json', 'w') as write:
		json.dump(send_data, write)

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

