import time, json, os, hashlib

def find_main_json_filename():
    main_json_file=[]
    for filename in os.listdir():
        if filename.find('.json') != -1:
            main_json_file.append(filename)
    #if len(main_json_file) > 1:
        #print("find more then one json file, Please delete the nonesance ones, but if you don't want I don't care I only reade the first one I find and this is your fald if its crash")
    #return main_json_file[0]
    return "test2.json"

def chack_and_coloect_the_json_filename(json_filename):
    with open(json_filename, 'r') as Read_file:
            return_json_file = json.load(Read_file)
    return return_json_file
    #return {}

def make_password_to_save(password):
    return hashlib.sha256(password.encode()).hexdigest()


def singin_form(input_data):
    send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
    show_data = {}
    show_data = {"private": {parts:input_data[parts] for parts in input_data if parts not in ["device_ip_address", "product_or_time_reservs", "username", "location"]}, "public": {parts:input_data[parts] for parts in input_data if parts in ["username", "email", "work", "location"]}, "send_requests_from_user": [], "profile_type": input_data["product_or_time_reservs"], "active_ip_address": [input_data["device_ip_address"]], "user_activation": "log-in", "requests_for_user": [], "products": []}
    if input_data["product_or_time_reservs"] == "sell_reserv_time" or input_data["product_or_time_reservs"] == "sell_both":
        show_data["timeline"] = []
    if input_data["location"] in [citi for citi in send_data]:
        send_data[input_data["location"]][input_data["username"]] = show_data
    else:
        send_data[input_data["location"]] = {}
        send_data[input_data["location"]][input_data["username"]] = show_data
    with open(find_main_json_filename(), "w") as Write_file:
        json.dump(send_data, Write_file)

def login_form(input_data):
    send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
    G_user_data = get_user_to(input_data["username"])
    if G_user_data != []:
        if G_user_data["password"] == input_data["password"]:
            send_data[G_user_data["public"]["location"]][input_data["username"]]["user_activation"] = "log-in"
            return {"ERROR": ""}
        else:
            return {"ERROR": "wrong_password"}
    else:
        return {"ERROR": "user_not_found"}
def show_the_user_wants_products(username):
    user_data = get_user_to(username)

def change_profile_D(user_name, main_user_data):
    send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
    send_data[get_user_to(user_name)["public"]["location"]][user_name] = main_user_data
    with open(find_main_json_filename(), "w") as Write_file:
        json.dump(send_data, Write_file)

#have to check the format I LOVE PROGRAMMING
def change_ip_add(username, ip_add):
	send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if name == username:
					if user[name][0]['ip'] != ip_add:
						user[name][0]['ip'] = ip_add
	with open(find_main_json_filename(), 'w') as W:
		json.dump(send_data, W)



def get_user_info_by_device_ip_add(ip_add):
	send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if user[name][0]['ip'] == ip_add: return name


def show_all_users_poblic_data_in_user_location(user_location):
	append_data = []
	send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
	for loc in send_data:
		if user_location == loc:
			for user in send_data[loc]:
				for name in user:
					append_data.append(user[name])
	return append_data

def get_user_to(usern):
    send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
    for citi in send_data:
        for user in send_data[citi]:
            if user == usern:
                return send_data[citi][user]

def delete_user(username):
	send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if username == name:
					send_data[citi].remove(user)

def LogOuT(username):
	send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
	for citi in send_data:
		for user in send_data[citi]:
			if user == username:
				send_data[citi][user]['user_activation'] = 'log-out'
	with open(find_main_json_filename(), 'w') as W:
		json.dump(send_data, W)

def login_active(username):
	send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if name == username:
					user[name][4]['user_activation'] = 'log-in'
	with open(find_main_json_filename(), 'w') as write_file:
		json.dump(send_data, write_file)

def login_m(username):
	send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
	for citi in send_data:
		for user in send_data[citi]:
			for name in user:
				if username == name:
					user[name]['user_activation'] = 'log-in'
	with open(find_main_json_filename(), 'w') as W:
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

def send_request(user, request_profile):
	send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
	request_full_data = {'request_address': request_profile[6],'request_from': request_profile[0], 'request_to': request_profile[1], 'time': request_profile[5], 'product': request_profile[2], 'product_numbers': request_profile[3], 'request_activ': 'request_sended'}
	for citi in send_data:
		for users in send_data[citi]:
			for name in users:
				if user == name:
					users[name][2]['requests'].append(request_full_data)
				elif from_user == name:
					users[name][3]['send_requests'].append(request_full_data)
	with open(find_main_json_filename(), 'w') as write_file:
		json.dump(send_data, write_file)

def change_user_information(username, user_data):
    send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
    for citi in send_data:
        for user in send_data[citi]:
            for Username in user:
                if Username == username:
                    user[Username] = user_data

def custom_time_line(username, user_data):
    send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
    change_user_information(username, user_data)

def sing_in():
	print('write your private information ["private key"]')
	name = input('Name: ')
	username = input('username: ')
	password = make_password_to_save(input('password: '))
	timeline = input('timeline: ')
	work = input('work: ')
	location = input('location: ')
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
    def __init__(self, user_username, send_user_username, product, product_numbers, product_price):
        self.send_user_username = send_user_username
        self.user_username = user_username
        self.product = product
        self.product_numbers = product_numbers
        self.product_price = product_price
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
    def make_request_profile(self):
        self.profile = [self.user_username, self.send_user_username, self.product, self.product_numbers, self.product_price, self.chose_file]
        self.profile.append(make_password_to_save(''.join([word for word in self.profile])))
        return self.profile
    def send_request_to_user_in_command_line(self):
        send_request(self.profile)
        print(f"\033[97m[INFO]\033[00m: {self.profile[6]} is sended to {self.send_user_username}")

def change_requets_act(username, request_address, change_act_val):
    request_profile=[F for F in get_user_to(username)[3]['send_requests'] if F['request_address'] == request_address][0]
    send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
    for citi in send_data:
        for name in send_data[citi]:
            if name==send_username:
                for request in get_user_to(name)[3]['send_requests']:
                    if request['request_address'] == request_address:
                        request['request_activ'] = change_act_val
            elif name==get_username:
                for request in get_user_to(name)[2]['requests']:
                    if request['request_address'] == request_address:
                        request['request_activ'] = change_act_val
    with open(find_main_json_filename(), 'w') as write_file:
        json.dump(write_file, send_data)

def show_all_products_and_reservs_in_user_citi(user_citi, username):
    send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
    return_data=[]
    for user in send_data[user_citi]:
        if user[1]['username'] != username:
            return_data.append(user[5])
    return return_data

class find_the_best_product:
    def __init__(self, user_location, product_type=""):
        self.user_location = user_location
        self.product_type = product_type
    def coloect_data_from_databse(self):
        self.main_use_data = [citi for citi in chack_and_coloect_the_json_filename(find_main_json_filename()) if citi == self.user_location]
    def find_all_products_in_location(self):
        self.main_use_data = []
        for citi in chack_and_coloect_the_json_filename(find_main_json_filename()):
            if citi == self.user_location:
                self.main_use_data.append(chack_and_coloect_the_json_filename(find_main_json_filename())[citi])
        return self.main_use_data
def check_time_requests(requests):
    return [TIME["time"] for TIME in requests if TIME["requests_activation"] not in ["canceld", "ended_selling", "not_selling_now"]]


def find_the_send_requests_and_cahnge_the_activation():
    pass
def get_time():
    return time.asctime()[11:19]

def today_date():
    re = f"{time.asctime()[:11]}{time.asctime()[20:]}"
    return re

def __check_num(Time):
    return Time[0:2]

#
#***********************************************************************************************
#***********************************************************************************************
#this is the old version
def json_singin(data):
    send_data = chack_and_coloect_the_json_filename(find_main_json_filename())
    username = data["username"]
    location = data["location"].split('/')[0]
    geuss = [table for table in send_data if table == location]
    data_send_json = {}
    data_send_json[username] = []
    data_send_json[username].append({'name': data["name"], 'username': username, 'password': data["password"], 'product_or_time_reservs': data["product_or_time_reservs"], 'work': data["work"], 'location': data["location"]})
    data_send_json[username].append({'name': data["name"], 'username': username, 'product_or_time_reservs': data["product_or_time_reservs"], 'work': data["work"], 'location': data["location"]})
    data_send_json[username].append({'requests_for_user': []})
    data_send_json[username].append({'send_requests_from_user': []})
    data_send_json[username].append({'user_activation': 'log-in'})
    if data["product_or_time_reservs"] == "sell_product" and data["product_or_time_reservs"] == "sell_both":
        data_send_json[username].append({'user_products': []})
    if geuss == []:
        send_data[location] = []
        send_data[location].append(data_send_json)
    else:
        send_data[geuss[0]].append(data_send_json)
    with open(find_main_json_filename(), 'w') as write:
        json.dump(send_data, write)

def Longin(username, password):
    if get_user_to(username) == None:
        return "user not found"
    else:
        if password == get_user_to(username)["private"]['password']:
            login_m(username)
            return "loggin_good"
        else:
            return 'wronge password'