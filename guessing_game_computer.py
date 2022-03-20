import random


# function that guess entered number generated randomly by computer
def guess(range):
    random_number = random.randint(1, range)
    guess = 0
    tries_count = 0

    while guess != random_number:
        guess = int(input("Enter your Guess: "))
        tries_count += 1

        if guess < random_number:
            print(" Guess again, Number is too low.....\n")
        else:
            print(" Guess again, Number is too High....\n")

    print(" Congrats, you Guessed the Number in {} tries!".format(tries_count))


# function that lets computer guess your number
def computer_guess(range):
    low = 1
    high = range
    feedback = ''
    tries_count = 0

    while feedback != 'c':
        if low == high:
            guess = high
        else:
            guess = random.randint(low, high)

        feedback = input(f"Number is {guess} How did I do it? is it higher(h), is it lower(l) or am I damn correct(c): ")
        tries_count += 1
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"See, I knew I can read your mind ;), but it took {tries_count} tries ofc")


choice = int(input("Let's Play the Guessing Game \n\
    Enter your Choice \n\
    1. Computer to Guess a Number \n\
    2. You Guess a Number \n"))
print()
range = 100
if choice == 1:
    computer_guess(range)
else:
    guess(range)
