import time

def sprint(statement, t=0.03, end_time=1, e='\n'):
	lines = statement.split('\n')
	for line in lines:
		to_print = ''
		for c in line:
			to_print += c
			print(f"{to_print}\r", end='')
			time.sleep(t)
		print(f"{e}", end='')
	time.sleep(end_time)

quit()
sprint("Hello, how is your day?\nWhat are you doing?")