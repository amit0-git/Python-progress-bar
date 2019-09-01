#Author:Amit Verma
import time
import sys

done = 'end'
def animate():
    while done == 'end':
        sys.stdout.write('\rLoading |')
        time.sleep(0.1)
        sys.stdout.write('\rLoading /')
        time.sleep(0.1)
        sys.stdout.write('\rLoading -')
        time.sleep(0.1)
        sys.stdout.write('\rLoading \\')
        time.sleep(0.1)
    

animate()

