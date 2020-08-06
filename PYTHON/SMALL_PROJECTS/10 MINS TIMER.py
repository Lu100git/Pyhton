import os
import time
x = 1
y = 1
z = True

while (x<= 600):
	print(y)
	time.sleep(0.5)
	x = x + 1 
	os.system("clear")
	time.sleep(0.5)
	y = y + 1
	if y == 60:
		y = 0
		print("1 min just passed")


while z:
	print("DONE!")
	print("10 mins just passed, timer is done")
	print("press any key to exit")
	enter = raw_input()		
	z = False
			
	
	
	

