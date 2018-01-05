import random

number = random.randint(1, 10)
print("im thinking of a number")

for i in range(1, 10):
    guess = int(input("Take a guess: "))
    if guess < number:
        print("your guess is too low")
    elif number > guess and ((number - guess) < 2):
        print("you are so close")
    elif number > (guess + 2):
        print("too high")
    else:
        break
if guess is number:
    print("good, you got it in " + str(i) + " guesses!")
else:
    print("nope, i was thinking of " + str(number))
