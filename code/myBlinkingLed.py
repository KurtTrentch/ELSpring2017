import RPi.GPIO as GPIO
import time
import signal
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def terminate(signal, frame):
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, terminate)

def rapid_blink():
	GPIO.output(17, True)
	time.sleep(.2)
	GPIO.output(17, False)
	time.sleep(.2)


def Blink():
	while True:
		for i in range(3):
			rapid_blink()
		time.sleep(5)
		for i in range(4):
			rapid_blink()
		time.sleep(5)
Blink()
