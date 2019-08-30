#Author:Amit Verma
import os 
import time

def loader():
	a=6
	while a>0:
		print('Loading [|]')
		time.sleep(.1)
		os.system('clear')
		print('Loading [/]')
		time.sleep(.1)
		os.system('clear')
		print('Loading [--]')
		time.sleep(.1)
		os.system('clear')
		print('Loading [\]')
		time.sleep(.1)
		
		os.system('clear')
		a-=1
loader()
