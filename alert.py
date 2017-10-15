#!/usr/bin/env python
import datetime
import subprocess 
import RPi.GPIO as GPIO 
import time
import os
import random
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

door1 = 19

GPIO.setup(door1, GPIO.IN, GPIO.PUD_UP)
now = datetime.datetime.now()
today6pm =  now.replace(hour=18, minute=0, second=0, microsecond=0)
today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
while True:
    
    now = datetime.datetime.now()
    today6pm =  now.replace(hour=18, minute=0, second=0, microsecond=0)
    today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
    now = datetime.datetime.now()
   
    
    #if now == now.replace(minute = 01, second = 0):
	# subprocess.call(['aplay "clock.wav"'], shell=True)
         #print ("playing clock chime")  
    if GPIO.input(door1) == False:
       print("Door 1 is closed.")
       #time.sleep(.1)
    elif GPIO.input(door1) == True and now > today6pm or GPIO.input(door1) == True and now < today8am:
       time.sleep(3)
       if GPIO.input(door1) == True:
           print("intruder") 
           subprocess.call(['aplay "police_s.wav"'], shell=True)	
    elif GPIO.input(door1) == True and now > today8am or GPIO.input(door1) == True and now < today6pm:
       time.sleep(.1)
       print("customer")
       subprocess.call(['aplay "bleep_01.wav"'], shell=True)
       time.sleep(12)       
   
GPIO.cleanup()
