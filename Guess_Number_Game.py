# ==========================================
# Internship Task: Guess the Number Game
# Developed By: [Your Name]
# Description:
# A simple number guessing game where
# the computer generates a random number
# and the user tries to guess it.
# ==========================================

import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

# Variable to count attempts
attempts = 0

print("===================================")
print("      GUESS THE NUMBER GAME       ")
print("===================================")

print("I have selected a number between 1 and 100.")
print("Try to guess the number!")

# ==========================================
# Game Loop
# ==========================================

while True:

    try:
        # User input
        guess = int(input("\nEnter your guess: "))

        # Increase attempt count
        attempts += 1

        # Check guess
        if guess < secret_number:
            print("📉 Too Low! Try a higher number.")

        elif guess > secret_number:
            print("📈 Too High! Try a lower number.")

        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number {secret_number} correctly.")
            print(f"Total Attempts: {attempts}")
            break

    except ValueError:
        print("❌ Please enter a valid number.")

print("\nThank You for Playing!")