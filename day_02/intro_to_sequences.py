"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = []



# Bug Exploration:
# Try printing foods[100] below.
# Q: What error do you get, and what does it mean?



# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()


# TODO: Insert a food at the beginning with .insert()


# TODO: Remove one food from the list with .remove()


# TODO: How many foods are in the list? Use len()


# Bug Exploration:
# Try removing something that isn’t in the list:
# foods.remove("chocolate")
# Q: What happens? Why?


# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.


# Bug Exploration:
# Change your loop to go past the length of the list:
#for i in range(______):
  #  print(f"Index {i} → {foods[i]}")
# Q: Why does this cause an error?


# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 
me = {
    "name": "Kevin",
    "age": 30,
    "student": False
    }

# TODO: Make a dictionary with at least 3 pieces of information about yourself.


# Access values using keys by using the .get() method rather than indexing
# print(f"My name is {me['name']}")
# print(f"My age is {me['age']}")
# print(f"My favorite color is {me['favorite_color']}")

# Bug Exploration:
# Try printing a key that doesn’t exist.
# print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?


# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.


# TODO: Change the value of an existing key.


# TODO: Remove one key-value pair.


# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?


# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()


# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)

# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?


# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.

dict_Test = {"Siddiqi": "Milk", "Lorcan": "Meat", "Artiom": "Cake"}

for key, value in dict_Test.items():
    print(f"{key} likes {value}")
# TODO: Print the favorite food of the second friend.

# TODO: Loop through and print "<name> likes <food>" for each friend.


# Bug Exploration:
# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?


# --- Section 8: Reflection ---
# Answer in comments:
# 1. How is a list different from a dictionary?
#dictionary uses key value pairs
# 2. When would you want to use a dictionary instead of a list?
#when you want speed or when you want key value pairs
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
#lists to contain list of numbers
#dictionary to hold index
# 4. What types of mistakes gave you the most errors today?

# 5. How might noticing errors actually help you learn?