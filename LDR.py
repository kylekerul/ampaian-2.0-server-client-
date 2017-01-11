import socket
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
def RCtime (ldr,led):
	reading = 0
	GPIO.setup(led, GPIO.OUT)
	#GPIO.output(led, GPIO.LOW)
	GPIO.setup(ldr, GPIO.OUT)
	GPIO.setup(ldr, GPIO.LOW)
	time.sleep(0.1)

	

	GPIO.setup(ldr, GPIO.IN)
	while (GPIO.input(ldr) == GPIO.LOW):
		reading += 1
		if(reading >= 3000):
			GPIO.output(led, GPIO.HIGH)
			#time.sleep(1)
		else:
			GPIO.output(led, GPIO.LOW)

		        		
	return reading	

	
s = socket.socket()        
host = "192.168.1.13" #socket.gethostname() 
port = 12225              
s.bind((host, port))   

s.listen(5)	
	
while(1):
	c, addr = s.accept()
	if c.recv(1024)=="ldr":
		print 'Client connected :', addr
		print"\n"
		while(1):
			print RCtime(23,18)
	else:
		break


