import random
highest = 10
answer = random.randint(1,highest)
print(answer) # TODO: Remove after testing
print(f'Please guess a number between 1 and {highest}: ')
guess = None # initialize to apply to while loop 

while guess != answer:
    guess = int(input())
    
    if guess == 0:
        print('Game over. -_-')
        break
    elif guess < answer:
        print('Please guess higher')
        continue
    elif guess > answer:
        print('Please guess lower')
        continue
    elif guess == answer:
        print('Well done, you guessed it')
        break
