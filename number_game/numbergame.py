
import random
def game():
    guesses = 0
    secret_num= int(input("Please input a secret number"))
    guess = random.randint(1, 100)

    while guesses < 7:

        if guess == secret_num:
            print("You got it! My number was {}".format(secret_num))
            break
        elif guess > secret_num:
            print('Your guess is too high, guess again {}'.format(guess))
            guess= random.randint(1,guess)
            guesses += 1
        else:
            print('Your guess is too low, guess again {}'.format(guess))
            guess= random.randint(guess,100)
            guesses += 1
    else:
            print("You lose, my number was {}".format(secret_num))


game()

