import pigpio, os, time

class Car:
	'''Handles communication with real car'''
	def __init__(self):
		self.speed_pin = speed_pin
		self.speed_direction_pin = speed_direction_pin
		self.steer_pin = steer_pin
		self.steer_direction_pin = steer_direction_pin
		
