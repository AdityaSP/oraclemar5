import random
r = random.randint(1,100)
print "I have tought of a number. Its your turn to guess."

guesses = 0
all_guesses = []
guess_str = ''
while True:
    user_guess = input('Enter your guess [1-100]: ')
    guesses = guesses + 1
    all_guesses.append(user_guess)
    guess_str = guess_str + ',' + str(user_guess)
    if user_guess < r:
        print "LOW"
    elif user_guess > r:
        print "HIGH"
    else:
        print "Bingo! You guessed it right!"
        print "You took", guesses, "guesses"
        print "These were your guesses", all_guesses
        print "Guess str", guess_str
        break