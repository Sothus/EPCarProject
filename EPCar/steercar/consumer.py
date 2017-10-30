from channels import Group
from steercar import car

controlled_car = car.Car()

def ws_connect(message):
	print('ws_connect')
	print('message')
	path = message['path']
	
	Group("steercar").add(message.reply_channel)
	message.reply_channel.send({
		"text": "You're connected to steercar group",
	})

#TODO - Check valid values for directions
def ws_message(message):
    global controlled_car

    print('ws_message')
    print("Received!" + message['text'])
	
    if(message['text'] == "steer_forward_1"):
        controlled_car.move(100, 1)
		
    elif(message['text'] == "stop_steer_forward_1"):
        controlled_car.stop_move()
		
    elif(message['text'] == "steer_forward_2"):
        controlled_car.move(150, 1)
		
    elif(message['text'] == "stop_steer_forward_2"):
        controlled_car.stop_move()
		
    elif(message['text'] == "steer_forward_3"):
        controlled_car.move(250, 1)
		
    elif(message['text'] == "stop_steer_forward_3"):
        controlled_car.stop_move()
		
    elif(message['text'] == "steer_forward_left_1"):
        controlled_car.turn(250, 1)
        controlled_car.move(100, 1)		
		
    elif(message['text'] == "stop_steer_forward_left_1"):
        controlled_car.stop_move()
        controlled_car.reset_turn()
		
    elif(message['text'] == "steer_forward_left_2"):
        controlled_car.turn(250, 1)
        controlled_car.move(200, 1)	
		
    elif(message['text'] == "stop_steer_forward_left_2"):
        controlled_car.stop_move()
        controlled_car.reset_turn()
		
    elif(message['text'] == "steer_forward_right_1"):
        controlled_car.turn(250, 0)
        controlled_car.move(100, 1)	
		
    elif(message['text'] == "stop_steer_forward_right_1"):
        controlled_car.stop_move()
        controlled_car.reset_turn()
		
    elif(message['text'] == "steer_forward_right_2"):
        controlled_car.turn(250, 0)
        controlled_car.move(250, 1)	
		
    elif(message['text'] == "stop_steer_forward_right_2"):
        controlled_car.stop_move()
        controlled_car.reset_turn()
		
    elif(message['text'] == "steer_backward_1"):
        controlled_car.move(100, 0)	
				
    elif(message['text'] == "stop_steer_backward_1"):
        controlled_car.stop_move()
		
    elif(message['text'] == "steer_backward_2"):
        controlled_car.move(150, 0)
		
    elif(message['text'] == "stop_steer_backward_2"):
        controlled_car.stop_move()
		
    elif(message['text'] == "steer_backward_3"):
        controlled_car.move(250, 0)
		
    elif(message['text'] == "stop_steer_backward_3"):
        controlled_car.stop_move()
		
    elif(message['text'] == "steer_backward_left_1"):
        controlled_car.turn(250, 1)
        controlled_car.move(100, 1)	
		
    elif(message['text'] == "stop_steer_backward_left_1"):
        controlled_car.stop_move()
        controlled_car.reset_turn()
		
    elif(message['text'] == "steer_backward_left_2"):
        controlled_car.turn(250, 1)
        controlled_car.move(200, 1)	
		
    elif(message['text'] == "stop_steer_backward_left_2"):
        controlled_car.stop_move()
        controlled_car.reset_turn()
		
    elif(message['text'] == "steer_backward_right_1"):
        controlled_car.turn(250, 0)
        controlled_car.move(100, 1)	
		
    elif(message['text'] == "stop_steer_backward_right_1"):
        controlled_car.stop_move()
        controlled_car.reset_turn()
		
    elif(message['text'] == "steer_backward_right_2"):
        controlled_car.turn(250, 0)
        controlled_car.move(250, 1)	
		
    elif(message['text'] == "stop_steer_backward_right_2"):
        controlled_car.stop_move()
        controlled_car.reset_turn()
	
def ws_disconnect(message):
	print('ws_disconnect')
	Group("sensor").discard(message.reply_channel)

