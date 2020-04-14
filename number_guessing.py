import random
start = input('Please enter the start of the random range: ')
end = input('Please enter the end of the random range: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
times = 0
while True:
	guess = input('Please type a number between the start and the end range: ')
	guess = int(guess)
	times = times + 1
	if guess == r:
		print('Correct guess!')
		print('This is the', times, 'times guessing.')
		break
	else:
		if guess > r:
			print('r is smaller.')
		elif guess < r:
			print('r is bigger.')
	print('This is the', times, 'times guessing.')
