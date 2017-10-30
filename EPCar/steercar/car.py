import pigpio, os, time

class Car:
	'''Handles communication with real car'''
	
	def __init__(self, car_name = "default car name",
	             mode_pin = 25, speed_pin = 14, speed_direction_pin = 15, 
	             steer_pin = 23, steer_direction_pin = 24):
		'''Creates all needed variables and configures GPIO'''
		
		self.car_name = car_name
						
		self.mode_pin = mode_pin
		self.speed_pin = speed_pin
		self.speed_direction_pin = speed_direction_pin
		self.steer_pin = steer_pin
		self.steer_direction_pin = steer_direction_pin
		self.pi = pigpio.pi()
		
		print("Initialisation started")
		self.pi.set_mode(self.speed_pin, pigpio.OUTPUT)
		self.pi.set_mode(self.speed_direction_pin, pigpio.OUTPUT)
		self.pi.set_mode(self.steer_pin, pigpio.OUTPUT)
		self.pi.set_mode(self.steer_direction_pin, pigpio.OUTPUT)
		self.pi.set_mode(self.mode_pin, pigpio.OUTPUT)
		print("Initialisation completed")
		
		
	def __str__(self):
		'''Returns car name'''
		
		class_str = "Car name: " + self.car_name
		return class_str
		
	
	def move(self, speed, direction):
		'''Car starts to move in given speed and direction (forward or backward)'''
		
		self.pi.write(self.speed_direction_pin, direction)
		self.pi.set_PWM_dutycycle(self.speed_pin, speed)
		
		
	def stop_move(self):
		'''Stops the car'''
		
		self.pi.write(self.speed_direction_pin, 0)
		self.pi.set_PWM_dutycycle(self.speed_pin, 0)
		
	def turn(self, steer_angle, steer_direction):
		'''Car starts to turn in choosen direction and angle'''
		
		self.pi.write(self.steer_direction_pin, steer_direction)
		self.pi.set_PWM_dutycycle(self.steer_pin, steer_angle)
		time.sleep(0.02)
		
		
	def reset_turn():
		'''Reset steer wheels to deafult position'''
		
		self.pi.write(self.steer_direction_pin, 0)
		self.pi.set_PWM_dutycycle(self.steer_pin, 0)
	
		
