
import random
def game():
    number = random.randint(1, 100)
    guesses = []

    while len(guesses) < 7:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("{} is not a number! Please guess again".format(guess))
        else:
            if guess == number:
                print("You got it! My number was {}".format(number))
                break
            elif guess > number:
                print("{} is too high, guess again".format(guess))
            else:
                print("{} is too low, guess again".format(guess))
            guesses.append(guess)
    else:
        print("You lose, my number was {}".format(number))

    play_again = input("Do you want to play again? Y/n")
    if play_again.lower() != 'n':
        game()
    else:
            print("See ya")

game()

