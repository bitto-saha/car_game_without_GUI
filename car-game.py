print("                        'car game without GUI'")


command = ""
is_started = False
while command.lower() != "quit":
	cmd = input(">").lower()
	if cmd == "start":
	
		if is_started:
			print("car is already started!")
		else:
			print("car started....")
			
	elif cmd == "stop":
		
		if not is_started:
			print("car is already stopped!")
		else:
			print("car stopped.....")
	elif cmd == "quit":
		command = "quit"
	elif cmd == "help":
		print('''
		start -- to start
		stop -- to stop
		quit -- to exit
		''')
	else:
		print("i don't understand that!")