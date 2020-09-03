def main_sercher(times, time_ss):
	send_time = []
	for time in times:
		for i in range(len(time)+1):
			if time[:i] == time_ss:
				send_data.append(time)
	return send_time

