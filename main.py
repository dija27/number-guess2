import random
correctAnswer = random.randint(1,100)
gameOver = False

while gameOver == False:

    playerGuess= int(input("guess a number between 1 and 100:"))


    if playerGuess == correctAnswer: 
        compareAnswer = "right"
        gameOver = True
    elif playerGuess > correctAnswer:
        compareAnswer = "high"
    elif playerGuess < correctAnswer:
        compareAnswer = "low"
    
    if compareAnswer == "right":
        print("correct1 you win!!")
    elif compareAnswer == "high":
        print("too hight! gess again!")
    elif compareAnswer == "low":
        print("too low! guess again!")
