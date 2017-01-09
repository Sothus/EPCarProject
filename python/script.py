import webiopi
import datetime

GPIO = webiopi.GPIO


LED = 17

def setup():
	GPIO.setFunction(LED, GPIO.OUT)

@webiopi.macro
def LightOn():
	GPIO.digitalWrite(LED, GPIO.HIGH)

@webiopi.macro
def LightOff():
	GPIO.digitalWrite(LED, GPIO.LOW)

def destroy():
	GPIO.digitalWrite(LED, GPIO.LOW)