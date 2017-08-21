from channels import Group
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
	
def ws_disconnect(message):
	print('ws_disconnect')
	Group("sensor").discard(message.reply_channel)
