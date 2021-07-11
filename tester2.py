import os
import time #library for sleep function
import RPi.GPIO as GPIO #library for Raspberry Pi output pins
import wiringpi #library for pwm control commands 
import subprocess
from time import localtime, strftime
wiringpi.wiringPiSetupGpio()    #initiate GPIO pins
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)  #initialize pin 18 as a PWM output
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)  #set pin 18 to 'milliseconds' mode
# divide down clock
wiringpi.pwmSetClock(192)   #set clock cycle speed of pwm output
wiringpi.pwmSetRange(2000)  #range of potential pwm pulses to pass to the servo motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
flag = 0
ctr = 0  
GPIO.cleanup()
subprocess.run(["sudo","./adxl345spi","-t","5","-s",str("VCS")+"_"+str(flag)+"_"+"1.5_3200_1.csv"])

