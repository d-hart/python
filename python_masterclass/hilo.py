low = 1
high = 1000

print(f'Please think of a number between {low} and {high}')
input('Press Enter to start the game')

guess = 1
# Can't use guess != answer as the while loop condition because we don't know what the answer is
while True: 
    guess = low + (high - low) //2
    high_low = input(f'My guess is {guess}. Should I guess higher or lower? '
                    'Enter h or l, or c if my guess was correct'.casefold())

    if high_low == 'h':
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
        pass
    elif high_low == 'l':
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
        pass 
    elif high_low == 'c':
        print(f'I got it in {guesses} guesses')
        break
    else:
        print('Please enter h, l, or c')
    guesses = guesses + 1