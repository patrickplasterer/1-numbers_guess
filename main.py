import random

start = int(input("Please select the range start: "))
stop = int(input("Please select the range end: "))

answer = random.randrange(start, stop)

guess = int(input("Please guess number: "))


while guess != answer:
    if guess > answer:
        guess = int(input("Too high. Please guess again: "))
    elif guess < answer:
        guess = int(input("Too low. Please guess again: "))

print("Success!")

