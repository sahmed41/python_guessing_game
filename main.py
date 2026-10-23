from random import randint

# Game settings
attempt = 0
attempt_limit = 5
high_thrushhold = 10
low_thrushhold = -(high_thrushhold)
# Computer guesssing a number
game_guess = 20
user_guess = 0

# Getting user guess
# try:
#     user_guess = int(input("Guess the number the computer thinks: "))
# except:
#     print("Please enter a number")

difference = game_guess - user_guess



while difference != 0 and attempt < attempt_limit :
    print("Attempt:", attempt + 1)
    # Getting user guess
    user_guess = input("Guess the number the computer thinks: ")
    if user_guess.lower() == 'x':
        print("Exiting the game...")
        exit()
    try:
        user_guess = int(user_guess)
    except:
        print("Please enter a number")

    difference = game_guess - user_guess


    if difference == 0:
        print("You Win!")
    elif difference > 0 and difference < high_thrushhold:
        print("Low")
    elif difference > high_thrushhold:
        print("Too low")
    elif difference < 0 and difference >  low_thrushhold:
        print("High")
    else:
        print("Too high")

    attempt += 1


print("The guess is", game_guess)

