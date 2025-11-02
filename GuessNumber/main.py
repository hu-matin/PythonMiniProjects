import random

rand = random.randint(1,10)
choice = int(input('Enter your gues number between 1-10: '))
	
if choice == rand:
	print('you won!')
	
else:
	print('You lose!')
	print(20*'-')
	print(f'Your choice was [{choice}]\nRobot choice was [{rand}]')
	print(20*'-')
