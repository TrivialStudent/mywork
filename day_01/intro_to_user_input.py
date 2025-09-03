"""
Lesson: Loops, Conditionals, and User Input
-------------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how programs can respond to user input.
"""

# --- Section 1: Getting Input from the User ---

# TODO: Ask the user for their name and store it in a variable
# name = input(____)

# TODO: Ask the user for their age and store it as an integer
# age = int(input(____))

# Print out a greeting
print("Hello,", )
print("You are",  "years old")


# --- Section 2: Conditionals with Input ---

# TODO: Check if the user is old enough to vote (18+)
# if ____:
#     print("You can vote!")
# else:
#     print("You cannot vote yet.")

# TODO: Ask the user for a number and check if it's even or odd
# num = int(input("Enter a number: "))
# if ____:
#     print("Even number")
# else:
#     print("Odd number")


# --- Section 3: Loops with Input ---

# Problem: You want to ask a user for 5 test scores and print them
# without loops, you'd have to write 5 separate inputs.  

# TODO: Try writing 5 input statements manually first (commented out)
# score1 = int(input("Score 1: "))
# score2 = int(input("Score 2: "))
# ...

# Question: How could a loop make this easier?


# --- Section 4: For Loops with Input ---

# TODO: Use a for loop to ask for 5 test scores and print each one
# Example starter:
# for i in range(____):
#     score = int(input("Enter score #" + str(i+1) + ": "))
#     print("You entered:", ____)


# --- Section 5: While Loops with Input ---

# TODO: Keep asking the user to enter a positive number
# until they actually do. Use a while loop.
# Example starter:
# num = int(input("Enter a positive number: "))
# while ____:
#     print("That is not positive. Try again!")
#     num = int(input("Enter a positive number: "))
# print("Thank you! You entered:", num)


# --- Section 6: Challenges ---

# 1. Ask the user for a number and tell them if it's divisible by 3, 5, or both
# 2. Ask the user for their favorite color repeatedly until they type "stop"
# 3. Create a mini grading program:
#     - Ask the user for scores until they type -1
#     - Keep track of how many scores are passing (>= 60)
#     - Print a summary at the end
count = 0
while True:
    user_input = int(input("Enter a score: "))
    if user_input >= 60:
        count+=1
    if user_input == -1:
        print(f"Total passing scores: {count}")
        break


# --- Section 7: Reflection ---
# 1. How does using input change the way your program works compared to fixed variables?
# 2. How do loops and conditionals work together when handling user input?
# 3. What are some real-world programs where loops + conditionals + input are all necessary?
