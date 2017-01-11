import socket           

s = socket.socket()        
host = '192.168.1.13'#socket.gethostname()
port = 12225             

s.connect((host, port))
while(1):
	z = raw_input("Enter something for the server: ")
	s.send(z) 

	if z == 'exit':
		break
		
    
