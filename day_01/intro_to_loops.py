"""
Lesson: Data Types, Variables, and Why Loops Are Necessary
----------------------------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice patterns.
"""

# --- Section 1: Variables and Data Types ---

# TODO: Create a variable called name that stores your name
name = "Lorcan"

# TODO: Create a variable called age that stores your age
age = 18
# TODO: Create a variable called pi that stores the value 3.14159
pi = 3.1415926

# Print each variable
print(f"Name: {name}" )
print(f"Age: {age}" )
print(f"Pi: {pi}" )


# --- Section 2: Why Loops? ---

# Imagine you want to print the numbers 1 through 10.
# First, try it the "long way".

print(1)
print(2)
print(3)

# TODO: Keep going until you reach 10

# Question for you:
#   What happens if I want to print 1 through 100? Or 1 through 1000?
#   Is it realistic to keep writing print statements forever?


# --- Section 3: For Loops ---
# TODO: Replace the repeated print statements above with a for loop.

# Example starter (fill in the blanks):
# for ___ in ___:
#     print(___)

for numbers in range(-10,11):
    print(numbers)


# Hint: What does range(start, stop) do?


# --- Section 4: While Loops ---
# A while loop repeats until a CONDITION is no longer true.

# TODO: Try to print numbers 1 through 10 using a while loop.

# Example starter:
# x = 1
# while ___:
#     print(___)
#     # TODO: Don’t forget to change x, or your loop will run forever!

count = 0
while count != 11:
    print(count)
    count += 1
# --- Section 5: Reflection ---
# Answer these questions (in comments):
# 1. Why is a loop better than writing 100 print statements?
#effienct
# 2. What does a loop REQUIRE in order to work?
#conditions to run
#    (Think: starting point, stopping condition, something that changes)
