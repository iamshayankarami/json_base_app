from flask import Flask, request, render_template, url_for, redirect, session, flash
import os, time
import urllib.request
from Back_end_main_service import *

app = Flask(__name__)
app.secret_key = 'shayan-karami-secret-key-for-flask'

def get_time():
	return time.asctime()[11:19]

def __check_num(Time):
	return Time[0:2]

def check_img_formath(filename):
    return '.' in filename and filename.rsplit('.')[1].lower() in set(['jpg', 'png', 'jpeg'])

@app.route('/', methods=['POST', 'GET'])
def main_page():
    if 'username' in session:
        #len_user_gets_requests = len([R for R in get_user_to(session['username'])[2]['requests'] if R['request_activ'] == "request_sended"])
        return render_template('main_show_page.html')#, LUGR=len_user_gets_requests)
    return render_template('welcome.php')

@app.route('/profile', methods=["GET", "POST"])
def index():
    if 'username' in session:
        username = session['username']
        if get_user_to(username)['user_activation'] == 'log-out':
            return redirect(url_for('login'))
        if get_user_to(username)["profile_type"] == "sell_both" or get_user_to(username)["profile_type"] == "sell_product":
            requests = get_user_to(username)["requests_for_user"]
        elif get_user_to(username)["profile_type"] == "sell_both" or get_user_to(username)["profile_type"] == "sell_reserv_time":
            requests = get_user_to(username)["timeline"]
        return render_template("profile.html", username=username, requests=requests)
    return render_template('welcome.php')

@app.route('/singin', methods=['GET', 'POST'])
def test_in_here():
    ip_address = request.remote_addr
    if request.method == 'POST':
        return_data = {"name": request.form["name"], "email": request.form["email"], "username": request.form["username"], "password": make_password_to_save(request.form["password"]), "work": request.form["work"], "product_or_time_reservs": request.form['job_product'], "location": request.form["location"], "device_ip_address": ip_address}
        singin_form(return_data)
        session["username"] = request.form["username"]
        return redirect(url_for("test_set_time_line"))
    return render_template('singin.html')

@app.route('/singin/set_time_line', methods=['POST', 'GET'])
def test_set_time_line():
    if "username" in session:
        #add ip_address checks
        main_data = get_user_to(session["username"])
        if request.method == 'POST':
            if main_data["product_or_time_reservs"] == "sell_reserv_time":
                timeline = time_line_for_every_day(request.form["timeline"])
                main_data["product_or_time_reservs"] = timeline
                change_profile_D(session["username"], main_data)
                return redirect(url_for('CUSTOM_TIMES'))
            if main_data["product_or_time_reservs"] == "sell_both" or main_data["product_or_time_reservs"] == "sell_product":
                new_product = {'product_name': request.form['product_name'], 'product_cpacity': request.form['product_cpacity'], 'product_price': request.form['product_price'], 'product_activ': 'new_product'}
                product_address = make_password_to_save(''.join([parts for parts in new_product]))
                new_product["product_address"] = product_address
                File = request.files['file']
                if File and check_img_formath(File.filename):
                    filename = product_address + ".jpeg"
                    File.save(os.path.join("/home/shayan/json_base_app/UPLOAD_FOLDER/PRODUCT_IMG", filename))
                    new_product['product_image'] = os.path.join("/home/shayan/json_base_app/UPLOAD_FOLDER/PRODUCT_IMG", filename)
                    if main_data["product_or_time_reservs"] == "sell_both":
                        main_data["reserv_timeline"] = time_line_for_every_day(request.form["timeline"])
                        change_profile_D(session["username"], main_data)
                        add_Request(session["username"], new_product)
                        return redirect(url_for("CUSTOM_TIMES"))
                    else:
                        #main_data["products"] = []
                        add_Request(session["username"], new_product)
                        return redirect(url_for("main_page"))
        return render_template("customize_selling.html", main_data=main_data)

@app.route('/custom_times', methods=['POST', 'GET'])
def CUSTOM_TIMES():
    if "username" in session:
        return_data = get_user_to(session["username"])
        if get_user_to(session["username"])["product_or_time_reservs"] == "sell_both":
            GTS = get_user_to(session["username"])["private"]["reserv_timeline"]
        else:
            GTS = get_user_to(session["username"])["product_or_time_reservs"]
        if request.method == 'POST':
            main_data = [element for element in request.form]
            main_data = main_data[:len(main_data)-1]
            if get_user_to(session["username"])["product_or_time_reservs"] == "sell_both":
                return_data["private"]["reserv_timeline"] = main_data
            else:
                return_data["private"]["product_or_time_reservs"] = main_data
            custom_time_line(username, return_data)
        return render_template('custom_times.html', re=GTS)

@app.route('/check_profile_type', methods=['POST', 'GET'])
def check_profile_type():
    if request.method == 'POST':
        if request.form['profile_type'] == "bussines":
            return redirect(url_for("test_in_here", user_profile_type="bussines"))
    return render_template("check_profile_type.html")

@app.route('/login', methods=['POST', 'GET'])
def LogiN():
    if request.form == 'POST':
        user_name = request.form["username"]
        password = make_password_to_save(request.form["password"])
        Longin(user_name, password)
    return render_template("login.html")

@app.route('/old_singin', methods=["GET", "POST"])
def singin():
    ip_add = request.remote_addr
    if request.method == 'POST':
        name = request.form["name"]
        work = request.form["work"]
        password = make_password_to_save(request.form["password"])
        username = request.form["username"]
        timeline = request.form["timeline"]
        location = request.form["location"]
        push_data=[name, username, password, timeline, location, work, ip_add]
        json_singin(push_data)
        session['username']=username
        return redirect(url_for('index'))
    return render_template("singin.html")

@app.route('/old_login', methods=["GET", "POST"])
def login():
	ip_add = request.remote_addr
	if request.method == "POST":
		username = request.form["username"]
		password = make_password_to_save(request.form["password"])
		if get_user_to(username)[0] == []:
			return 'username not founded'
		else:
			if password == get_user_to(username)[0]['password']:
				#change_ip_add(username, ip_add)
				login_m(username)
				session['username']=username
				return redirect(url_for('index'))
			else:
				return 'wronge password'
	return '''<center>
	<form method='POST'>
		<p>username</p><input type='text', name='username'><br><p>password</p><input type='password' name='password'><br><input type='submit' name='submit' id='submit'>
	</form>
</center>
'''

@app.route('/show_all')
def SHOW_ALL():
	#ip_add = request.remote_addr
	if 'username' in session:
		username=session['username']
		user_data=get_user_to(username)
		show_data = show_all_users_poblic_data_in_user_location(user_data[1]['location'])
		return ''.join([f'''<a href={url_for('show_user', show_username=users[1]['username'])}>{users[1]['username']} </a><b>{users[1]['work']} </b><br><br>''' for users in show_data if users[1]['username'] != username])
	return redirect(url_for('index'))


@app.route('/show_data_of', methods=['POST', 'GET'])
def show_user():
    if 'username' in session:
        show_username = request.args.get('show_username', None)
        username = session['username']
        status = send_Request(username, show_username)
        timelines = status.check_time_line()
        if request.method == 'POST':
            select = request.form.get('select_form_time')
            status.chose_time_to_send(select)
            status.send_request_to_user_in_command_line()
            return redirect(url_for('show_my_send_requests'))
        return render_template('show_all.html', time_line=timelines)
    return redirect(url_for('index'))

@app.route('/show_my_send_requests', methods=['POST', 'GET'])
def show_my_send_requests():
    if 'username' in session:
        all_of_my_request = get_user_to(session['username'])[3]['send_requests']
        send_text = []
        for re in all_of_my_request:
            send_text.append([f"{re['request_to']} {re['time']} {re['request_activ']}", make_password_to_save(f"{re['request_to']} {re['time']} {re['request_from']}")])
        return render_template('show_my_sends_requets.html', data=send_text)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
	#ip_add = request.remote_addr
	if 'username' in session:
		LogOuT(session['username'])
		session.pop('username', None)
		return redirect(url_for('index'))
	return redirect(url_for('index'))

@app.route('/add_new_product', methods=['POST', 'GET'])
def add_new_product():
    if "username" in session:
        user_data = get_user_to(session["username"])
        if request.method == 'POST':
            new_product = {"product_seller": session["username"], 'product_name': request.form['product_name'], 'product_cpacity': request.form['product_cpacity'], 'product_price': request.form['product_price'], 'product_activ': 'new_product'}
            product_address = make_password_to_save(''.join([parts for parts in new_product]))
            File = request.files['file']
            if File and check_img_formath(File.filename):
                filename = product_address + ".jpeg"
                File.save(os.path.join("/home/shayan/json_base_app/UPLOAD_FOLDER/PRODUCT_IMG", filename))
                new_product["product_address"] = product_address
                new_product["product_image"] = os.path.join("/home/shayan/json_base_app/UPLOAD_FOLDER/PRODUCT_IMG", filename)
                user_data["products"].append(new_product)
                change_profile_D(session["username"], user_data) 
                return redirect(url_for("index"))
    return render_template('add_new_product.html')

if __name__ == '__main__':
	app.run("0.0.0.0", port=4000, debug=True)
