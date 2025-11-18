import random
print("welcome to guess the number")
print ("try to guess the number (1 - 100)")
print("can you guess what it is ")
number_to_guess = random.randint(1, 200)
input(number_to_guess)
if number_to_guess > 100:
    print("too low !")
if number_to_guess < 100:
    print("too high!")