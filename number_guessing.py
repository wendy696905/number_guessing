import random

r = random.randint(1, 100)
times = 0
while True:
	guess = input('Please type a number between 1 and 100: ')
	guess = int(guess)
	if guess == r:
		print('Correct guess!')
		break
	else:
		if guess > r:
			print('r is smaller.')
		elif guess < r:
			print('r is bigger.')
	times = times + 1
	print('This is the', times, 'times guessing.')
