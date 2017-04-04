#!/usr/bin/env python

import subprocess 
import RPi.GPIO as GPIO 
import time
import os
import random
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

#LED1 = 18
#LED2 = 23
door1 = 19
#door2 = 16


#GPIO.setup(LED1, GPIO.OUT)
#GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(door1, GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(door2, GPIO.IN, GPIO.PUD_UP)

#GPIO.output(LED1, 0)
#GPIO.output(LED2, 0)

while True:
    if GPIO.input(door1) == False:
       print("Door 1 is closed.")
       time.sleep(.1)
    else:
	
  	#if GPIO.input(door1) == True:
       		#print("Door 1 is open.")
		#x = random.randint(0,2)
		#if x == 0:
		#	subprocess.call(['aplay /home/pi/Downloads/135499__compusician__halloween-002-wav-120b.wav'], shell=True)
		#if x == 1:
       subprocess.call(['aplay "/home/pi/bleep_01.wav"'], shell=True)
                #if x == 2:
                 #       subprocess.call(['aplay /home/pi/Downloads/348859__robinhood76__06721-long-scary-hinge-creak.wav'], shell=True)
                
		#os.system('aplay /home/pi/Downloads/135499__compusician__halloween-002-wav-120b.wav')
       time.sleep(12)       
    #if GPIO.input(door2) == False:
       #print("Door 2 is closed.")
   #time.sleep(2)
    #else:
   #if GPIO.input(door2) == True:
       #print("Door 2 is open.")
       #time.sleep(5)
GPIO.cleanup()
