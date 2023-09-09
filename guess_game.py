import random
import math


lesser = int(input("Enter lesser number:- "))

higher = int(input("Enter higher number:- "))


x = random.randint(lesser, higher)
print("\n\tYou've only ",
	round(math.log(higher - lesser + 1, 2)),
	" chances to guess the integer!\n")

count = 0

while count < math.log(higher - lesser + 1, 2):
	count += 1

	guess = int(input("Guess a number:- "))

	if x == guess:
		print("Congratulations you guessed rightly in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

if count >= math.log(higher - lesser + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Try again next time!")
