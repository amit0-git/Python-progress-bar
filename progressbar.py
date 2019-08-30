#Simple progress bar
import os
import time


def pgbar():
	
	a=''
	for i in range(1,51):
		print('\033[0;33;43m',a.zfill(i),'\033[0m',i*2,'%')
		time.sleep(.1)
		os.system('clear')
pgbar()