# lab 4 
# Created by Chirag Wadhwani(cw844) and Karthik D.(kd453)
# This program is used to blink an LED using Python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)  # Set to BCM Mode
GPIO.setup(26, GPIO.OUT)  # Set to output mode 
pwm = 99	
p = GPIO.PWM(26, pwm) # Set to PWM
cur = time.time()
while True and time.time - cur > 10:  # Loop to continously blink and break after 10 seconds
	p.start(pwm)
	time.sleep(2)
	p.stop()
GPIO.cleanup()  
