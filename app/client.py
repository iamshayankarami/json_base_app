import socket, select, pickle
HEAERESIZE=10

server = s.socket.socket(socket.AF_INET, socket.SOCK_STRAM)
server.connect((socket.gethostname(), 7070))
server.listen(5)

while True:
	client, address = server.accept()
	

