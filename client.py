import socket   
import sys
from select import select  
import time      

s = socket.socket()        
host = "192.168.1.11" #socket.gethostname()
port = 12221             

s.connect((host, port))
#timeout = 3
z = raw_input("Enter Command : ")
s.send(z)
try:
	while(1):
		if z == "exit":
			break
		while(1):
			print s.recv(1024),"\nTIME : ",time.strftime("%H:%M:%S"),"\nDATE : ",time.strftime("%d/%m/%Y")
			
	
except KeyboardInterrupt:
		print"EXIT."
