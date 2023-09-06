import random
random.randint(0,6)
a= ("1","2","3","4","5")

def guess_number():
    secret_number = random.randint(1, 6)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 5: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

guess_number()