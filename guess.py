import random
mini = input ('please enter the lower limit')
maxi = input ('please enter the upper limit')
mini = int (mini)
maxi = int (maxi) 
r = random.randint(mini,maxi)
i = 0
while True :
	num = input ('please guess the number')
	num = int (num)
	if num == r :
		print('correct!')
		break
	else:
		i = i + 1
		print (i,' attempts have been used')
		if num > r :
			print ('the number guessed is greater')
		if num < r :
			print ('the number guessed is smaller')