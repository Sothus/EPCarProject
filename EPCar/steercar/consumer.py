from channels import Group
import pigpio
import time

SPEED = 14
DIRECTION = 15
STEER = 23
STEER_DIRECTION = 24
MODE = 25
pi = pigpio.pi()
pi.set_mode(SPEED, pigpio.OUTPUT)
pi.set_mode(DIRECTION, pigpio.OUTPUT)
pi.set_mode(STEER, pigpio.OUTPUT)
pi.set_mode(STEER_DIRECTION, pigpio.OUTPUT)
pi.set_mode(MODE, pigpio.OUTPUT)
pi.write(MODE, 1)
pi.write(DIRECTION, 0)
pi.write(STEER, 0)
pi.write(STEER_DIRECTION, 0)
pi.write(SPEED, 0)

def ws_connect(message):
	print('ws_connect')
	print('message')
	path = message['path']
	
	Group("steercar").add(message.reply_channel)
	message.reply_channel.send({
		"text": "You're connected to steercar group",
	})

def ws_message(message):
	print('ws_message')
	print("Received!" + message['text'])
	if(message['text'] == "steer_forward_1"):
		pi.set_PWM_dutycycle(SPEED, 100)
		
	elif(message['text'] == "stop_steer_forward_1"):
		pi.set_PWM_dutycycle(SPEED, 0)
		
	elif(message['text'] == "steer_forward_2"):
		pi.set_PWM_dutycycle(SPEED, 150)
		
	elif(message['text'] == "stop_steer_forward_2"):
		pi.set_PWM_dutycycle(SPEED, 0)
		
	elif(message['text'] == "steer_forward_3"):
		pi.set_PWM_dutycycle(SPEED, 250)
		
	elif(message['text'] == "stop_steer_forward_3"):
		pi.set_PWM_dutycycle(SPEED, 0)
		
	elif(message['text'] == "steer_forward_left_1"):
		pi.set_PWM_dutycycle(SPEED, 100)
		pi.set_PWM_dutycycle(STEER, 250)
		pi.write(STEER_DIRECTION, 1)
		
	elif(message['text'] == "stop_steer_forward_left_1"):
		pi.set_PWM_dutycycle(SPEED, 0)
		pi.set_PWM_dutycycle(STEER, 0)
	
def ws_disconnect(message):
	print('ws_disconnect')
	Group("sensor").discard(message.reply_channel)

