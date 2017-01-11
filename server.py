import socket
import time
from time import sleep 
import os
import RPi.GPIO as GPIO

#GPIO.input(26)==True , The door is close , else is open
#GPIO.input(12)==True , Fine Weather , else is raining


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # set to bcm : GPIO PIN
GPIO.setup(26, GPIO.IN, GPIO.PUD_UP) # PIN MAGNET SENSOR : set up pin 26



s = socket.socket()        
host = "192.168.1.11" #socket.gethostname() 
port = 12221               
s.bind((host, port))   

s.listen(5)




Motor1 = 23    # Input Pin pin7_IC
Motor2 = 24    # Input Pin pin2_IC
Motor3 = 25    # Enable Pin pin1_IC

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)
#pwm=GPIO.PWM(25,100) 
GPIO.setup(12, GPIO.IN)


 
def open(Motor1,Motor2,Motor3):   
 # pwm.start(100)
  GPIO.output(Motor1,GPIO.LOW)
  GPIO.output(Motor2,GPIO.HIGH)
  GPIO.output(Motor3,GPIO.HIGH)
  sleep(2)
  GPIO.output(Motor2,GPIO.LOW) 
  sleep(2) 
  
   
    
def close(motor1,motor2,motor3):
  GPIO.output(Motor1,GPIO.LOW)
 # pwm.start(100)
  GPIO.output(Motor1,GPIO.HIGH)
  GPIO.output(Motor2,GPIO.LOW)
  GPIO.output(Motor3,GPIO.HIGH)
  sleep(2)
  GPIO.output(Motor1,GPIO.LOW) 
  sleep(2)


while True:
 c, addr = s.accept()
 print 'Client connected :', addr
 print"\n"
 #print c.recv(1024)
 message = "The program is running.\n"
 F = "\nSTATUS : FINE WEATHER"
 R = "\nSTATUS : RAINING"
# P = 1
# L = 0
 #q = raw_input("Enter something to this client: ")
 if (c.recv(1024)=="run"):
  print(message)
  print"------------" 
  
  if (GPIO.input(26) == True):
   #c.send(R)
   if(GPIO.input(12)==False):
	#print"RAINING!"  
	c.send(R)
   
   while(1):
	  while (GPIO.input(12) == True):
		#print "Fine Weather!"
		c.send(F)
		open(Motor1,Motor2,Motor3)
		x=1
		while (x==1):
			#print "FINE WEATHER!"
			if (GPIO.input(12) == False):
				c.send(R)
				close(Motor1,Motor2,Motor3)
				y=1
				while(y==1):
					#print "RAINING!"
					if (GPIO.input(12) == True):
						x=0
						y=0	

       	
  elif (GPIO.input(26) == False):
   if(GPIO.input(12)==True):
	#print"FINE WEATHER!"
	c.send(F)
   while(1):
          while (GPIO.input(12) == False): #if raining
                close(Motor1,Motor2,Motor3) #the roof is close
		c.send(R)
                x=1
                while (x==1): #in condition ready to open roof
                        #print "RAINING!"
                        if (GPIO.input(12) == True): #if fine weather
                                open(Motor1,Motor2,Motor3) #the roof is open
				c.send(F)
                                y=1
                                while(y==1):
                                        #print "FINE WEATHER!"
                                        if (GPIO.input(12) == False): #if raining
                                                x=0
                                                y=0
												
												
												
												
  elif (GPIO.input(26) == True):
   if(GPIO.input(12)==True):
	#print"FINE WEATHER!"  
	c.send(F)
	open(Motor1,Motor,Motor3)
   
   while(1):
	  while (GPIO.input(12) == False):
		#print "RAINING!"
		c.send(R)
		close(Motor1,Motor2,Motor3)
		x=1
		while (x==1):
			if (GPIO.input(12) == True):
				c.send(F)
				open(Motor1,Motor2,Motor3)
				y=1
				while(y==1):
					if (GPIO.input(12) == False):
						x=0
						y=0		

  elif (GPIO.input(26) == False):
   c.send(R)
   if(GPIO.input(12)==False):
	#c.send(R)  
	close(Motor1,Motor2,Motor3)
	
	
   
   while(1):
	  while (GPIO.input(12) == True):
		#print "FINE WEATHER!"
		open(Motor1,Motor2,Motor3)
		c.send(F)
		x=1
		while (x==1):
			if (GPIO.input(12) == False):
				close(Motor1,Motor2,Motor3)
				c.send(R)
				y=1
				while(y==1):
					if (GPIO.input(12) == True):
						x=0
						y=0							
	
 elif (c.recv(1024)=="exit"):
		print"Server Closed."
		break 
  
