import random

r = random.randint(1,100)


while True:
	ans=input('請猜一波數字')

	if r==int(ans):
		print('你他媽終於答對囉!')
		break
	elif r > int(ans):
		print('比你答案大')
	elif r < int(ans):
		print('比你答案小')	

