import random
guess=random.randint(1,100)
while True:
    user_guess=int(input('guess the number between 1 and 100: '))
    if guess==user_guess:
        print('congrats, you guessed the number')
        break
    elif guess>user_guess:
        print('your guess is bit small!')
    elif guess<user_guess:
        print('your guess is bit big')
    else:
        print('please enter a valid guess')

