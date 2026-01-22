import random
guess=random.randint(1,100)
while True:
    try:
        user_guess=int(input('guess the number between 1 and 100:'))
        if guess>user_guess:
            print('your guess is bit low!')
        elif guess<user_guess:
            print('your guess is bit big')
        else:
            print('congrats, you guessed the number')
            break
    except ValueError:
        print('please enter a valid guess')

 
