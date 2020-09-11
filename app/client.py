import socket, select, pickle
from app import *
HEAERESIZE=10

server = s.socket.socket(socket.AF_INET, socket.SOCK_STRAM)

def fined_object_in_device(input_code):
	data = pickle.loads(input_code)['object']
	finder = Finder(data)

def send_data_to_find_obj(input_code):
	with server.connect((ip, port)) as S:
		S.send(pickle.dumps({'object': input_code}).encode())

