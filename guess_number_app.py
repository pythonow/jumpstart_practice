import random

def intro():
    print("-------------------------------------")
    print("      GUESS THE NUMBER APP")
    print("-------------------------------------")

def guess_number():

    guess = -1
    target = random.randint(0, 100)
    counter = 0

    while guess != target:

        guess_text = int(input("Guess a number between 0 and 100: "))
        guess = guess_text

        if guess_text < target:
            print("TOO LOW")
            counter += 1
        elif guess_text > target:
            print("TOO HIGH")
            counter += 1
        else:
            counter += 1
            print("CORRECT, YOU GUESSED RIGHT IN {} GOES".format(counter))

def main():
    intro()
    guess_number()

main()