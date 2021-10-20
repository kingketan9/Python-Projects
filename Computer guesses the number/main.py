import random

def comp_guess(x):
    guesses = 0
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if(low != high):
            guess = random.randint(low,high)
        else:
            guess = high # high = low
        feedback = input(f"Is {guess} too high(h), too low(l), or correct(c)")
        if(feedback == 'h'):
            high = guess - 1
        elif(feedback == 'l'):
            low = guess + 1
        guesses = guesses + 1

    print(f"The computer guessed your number,{guess} in {guesses} guesses correctly!")
comp_guess(1000)