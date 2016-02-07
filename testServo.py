#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

frequency = 100 # In Hz
pwm = GPIO.PWM(23, frequency) # Pin 23
pwm.start(15) # 15% of 100Hz, which is 1.5ms

#def move(angle):
#    duty = float(angle) / 10.0 + 2.5
#    print "Duty:", duty
#    pwm.ChangeDutyCycle(duty)

def move(angle):
    # For my particular servo, the angle is -65...65
    # Experimentation indicates that we want to set pulse width to 1ms for -65, 1.2ms for 0, and 2.3ms for 65
    # We want duty to be expressed as a percentage of frequency.
    # So that is 1% of the 100Mhz frequency for -65, 12% for 0, and 23% for 65 degrees
    duty = (11.0*float(angle)/65.0) + 12
    print "Duty:", duty
    pwm.ChangeDutyCycle(duty)


for i in [-65, -30, 0, 30, 65]:
    print "Moving to", i, "degrees"
    move(i)
    time.sleep(3)

GPIO.cleanup()
