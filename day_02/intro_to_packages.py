"""
Python Lab Activity: Packages, Documentation, and a Complex Number Guesser Game

Objective:
- Practice importing and using Python packages
- Learn how to read and explore package documentation
- Use input, loops, and conditionals
- Build a Complex Number Guesser Game

Instructions:
Work through each level in order. Follow the comments, read documentation
with help(), and fill in the TODOs. Test your code after each level.
"""

# ---------------------------------------------------
# Level 1 – Importing a Package
# Task:
# 1. Import the `random` module
# 2. Use help(random) to explore documentation
# 3. Print 3 random integers between 1 and 10
# ---------------------------------------------------

import random
# TODO: Print the square root of -1 using cmath


# ---------------------------------------------------
# Level 3 – User Input Basics
# Task:
# 1. Ask the user to type their name
# 2. Print a welcome message
# ---------------------------------------------------

# TODO: Ask for the user’s name and print a greeting


# ---------------------------------------------------
# Level 4 – Converting Input to Numbers
# Task:
# 1. Ask the user to enter a number
# 2. Convert it to an integer
# 3. Multiply it by 2 and print the result
# ---------------------------------------------------

# TODO: Ask for a number, convert it to int, double it, and print


# ---------------------------------------------------
# Level 5 – Random Complex Numbers
# Task:
# 1. Generate a random integer (-10 to 10) for the real part
# 2. Generate a random integer (-10 to 10) for the imaginary part
# 3. Construct a complex number and print it
# ---------------------------------------------------

# TODO: Generate a random complex number with integer real and imaginary parts


# ---------------------------------------------------
# Level 6 – Complex Number Guesser Game
# Rules:
# 1. Computer picks a random complex number (real and imaginary parts between -5 and 5)
# 2. User must guess both parts correctly
# 3. After each guess, provide feedback:
#    - "Too high" or "Too low" for each part
#    - If both are correct, the game ends
# 4. Repeat until correct
# ---------------------------------------------------

target_real = random.randint(-5, 5)
target_imag = random.randint(-5, 5)
target = complex(target_real, target_imag)

print("Welcome to the Complex Number Guesser Game!")
print("I have chosen a complex number with real and imaginary parts between -5 and 5.")

# TODO: Write a loop where the user keeps guessing until correct
# Hints:
# - Ask separately for real and imaginary guesses
# - Convert inputs to integers
# - Use if/else to give “too high” / “too low” feedback


# ---------------------------------------------------
# Extensions (Optional)
# - Limit the number of guesses
# - Give hints about magnitude (abs(z)) or angle (cmath.phase(z))
# - Let the user guess in the format "a+bj" and parse it as complex
# ---------------------------------------------------