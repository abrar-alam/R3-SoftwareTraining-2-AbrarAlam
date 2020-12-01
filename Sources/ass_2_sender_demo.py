import pickle
import socket
import time


pickle_in = open("dict.pickle","rb")
solution = pickle.load(pickle_in) # We loaded our solution path list

current_orientation = 0 # 0 ~ downwards, 1 ~ Upwards, 2 ~ right, 3 ~ left
						# since at the beginning thye orientation is down
current_index = 0; #This stores the index of our current position within solution list

#helper functions
def left_open():
	if (solution[current_index+1][0] < solution[current_index][0]):  
		return True
	else:
		return False

def right_open():
	if (solution[current_index+1][0] > solution[current_index][0]):  
		return True
	else:
		return False

def down_open():
	if (solution[current_index+1][1] > solution[current_index][1]):  
		return True
	else:
		return False

def top_open():
	if (solution[current_index+1][1] < solution[current_index][1]):  
		return True
	else:
		return False

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

stop = "[0][0][0][0]"
forward = "[255][0][255][0]"
turn_right = "[0][255][255][0]"
turn_left = "[255][0][0][255]"
backward = "[0][255][0][255]"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

for i in range (0, len(solution)):
	if(i == len(solution)-1):# we reached the end, thus we stop all the motor
		s.sendall(bytes(stop, "utf8"))
	else:
		if ((current_orientation == 0) and down_open()):
			s.sendall(bytes(forward, "utf8"))
			time.sleep(1) # We delay for 1 sec.

s.close()
		 



