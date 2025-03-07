from random import randint


def guess_game():
    guess_left = 3
    num = randint(1, 20)
    previous_guesses = []

    while guess_left != 0:
        try:
            guess = int(input(f'Guess a number (1-20).\n You have {guess_left} guesses left: '))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess in previous_guesses:
            print("You already guessed that number! Try another one.")
            continue
        previous_guesses.append(guess)

        if guess == num:
            print(f'Congrats!!! You guessed correctly')
            break
        elif guess < num:
            print("Too low. Try again")
        else:
            print("Too high. Try again")

        guess_left -= 1

    if guess_left == 0:
        print(f'Sorry the number was {num}.')

guess_game()
