import random

print("Hello World!")

print("Welcome to Lotto")

number = random.randint(1, 100)
guess = None
attempts = 0
limit = 5

print("Guess the number between 1 and 100.")
print(f"You have {limit} attempts.")

while guess != number and attempts < limit:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
if guess == number:
    print("Congratulations you Won!")
else:
    print(f"Sorry again next time, the number was {number}")