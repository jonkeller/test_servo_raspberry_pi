Some quick code to control a servo motor from a Raspberry Pi.

Accompanying video: https://youtu.be/tqRUMtgY-iI

The code was adapted from http://razzpisampler.oreilly.com/ch05.html but I removed the GUI and adapted the numeric parameters to work with my particular servo.

Update:
The original version, testServo.py, uses RPi.GPIO. The servo is very jittery. I checked this with my oscilloscope, and the problem was variance in the timing of the pulses from the Pi...even after killing X, MySQL, etc.

So, I added a new version, testServo_RPIO.py, which uses RPIO. There is much, much less jitter since it's using DMA rather than software timing. Before running this, just follow the RPIO installation instructions at https://pythonhosted.org/RPIO/
