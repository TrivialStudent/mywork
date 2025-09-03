###################################################################
# Core Python Walkthrough                                         #
#                                                                 #
# Focus: Functions, Classes, Documentation, and Code Organization #
# Goal: Understand why modular programming is useful              #
###################################################################

# 1. REPETITION AND BUGS
# -----------------------
# Imagine you are asked to calculate the area of rectangles with different sides.

# First attempt: copy-paste code for each rectangle.
width1 = 5
height1 = 10
print(f"Rectangle 1 area: {width1 + height1}")

width2 = 3
height2 = 7
print(f"Rectangle 2 area: {width2 + height2}")

width3 = 9
height3 = 2
print(f"Rectangle 3 area: {width3 + height3}")

# Problem: What if you realize you wrote the wrong formula?
# You’d have to go fix it in EVERY place.

# Task: Find the bug and make sure to fix it in every place.


# 2. FUNCTIONS TO THE RESCUE
# ---------------------------
# Functions save you from repetition and reduce bugs.
# A function is like a mini-program inside your program.
# You give it input values (called PARAMETERS),
# and it can send back an output value (called a RETURN VALUE).

def area_of_rectangle(width: int, height: int) -> int:
    """
    Calculate the area of a rectangle.

    Parameters:
        width (int): how wide the rectangle is
        height (int): how tall the rectangle is

    Returns:
        int: the area of the rectangle (width * height)
    """
    return width * height

print(f"Rectangle 1 area: {area_of_rectangle(5, 10)}")
print(f"Rectangle 2 area: {area_of_rectangle(3, 7)}")
print(f"Rectangle 3 area: {area_of_rectangle(9, 2)}")

# Challenge: Add a new function area_of_circle(radius) with proper docstring.


# Example function WITHOUT a return value
def print_welcome_message(student_name: str) -> None:
    """
    Print a welcome message for a student.

    Parameters:
        student_name (str): the name of the student to welcome

    Returns:
        None
    """
    print(f"Welcome to class, {student_name}! We are glad you are here.")

print_welcome_message("Jordan")
print_welcome_message("Taylor")

# Notice:
#   • This function does not calculate anything.
#   • It is still useful because it organizes a repeated task.
#   • Functions can be for calculation (returning values) OR for organization/printing.


# 3. CLASSES: DATA + BEHAVIOR TOGETHER
# -------------------------------------
# Functions are great, but sometimes you need to keep track of related data.
# That’s where classes come in.

class Rectangle:
    """
    A rectangle shape defined by width and height.

    Attributes:
        width (int): how wide the rectangle is
        height (int): how tall the rectangle is
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        """
        Compute the area of this rectangle.

        Returns:
            int: the area (width * height)
        """
        return self.width * self.height

    def describe(self) -> None:
        """
        Print a description of the rectangle.

        Returns:
            None
        """
        print(f"Rectangle {self.width} by {self.height} has area {self.area()}")

# Using the class:
r1 = Rectangle(5, 10)
r2 = Rectangle(3, 7)
r1.describe()
r2.describe()

# ⚠️ Challenge: Introduce a bug by returning width + height instead of width * height.
# Then fix it ONCE and see that all rectangles are correct again.


# 4. DOCUMENTATION MATTERS
# -------------------------
# Good docstrings help *other programmers* (and your future self) understand your code.
#   • Always state the purpose of the function/class
#   • List parameters with types
#   • List return values with type


###############################################
# HOMEWORK / PROJECT CHALLENGE
# -----------------------------
# Now that you've practiced functions, classes, and docstrings,
# it's time to start your own modular project.

# Instructions for students:
# 1. Create a NEW folder for your Shape Toolkit project.
# 2. Inside that folder, create three files:
#      - shapes.py
#          * Define at least three classes: Rectangle, Circle, Triangle
#          * Each class should have attributes, area() method, and describe() method
#      - utils.py
#          * Create helper functions, e.g., convert cm^2 to m^2
#          * Compare areas of two shapes
#      - main.py
#          * Import classes from shapes.py
#          * Import helper functions from utils.py
#          * Allow user to create shapes (input dimensions)
#          * Print area and descriptions
# 3. Make sure every function and class has proper docstrings
# 4. Run main.py to see interactive results
# 5. Optional Bonus:
#      - Add a welcome function in main.py (no return value) that explains available shapes
#      - Allow user to choose which shapes to create dynamically

# Deliverable:
#   - One organized folder
#   - Three files (shapes.py, utils.py, main.py)
#   - Proper use of functions with and without return values
#   - Proper use of classes and docstrings
#   - Modular, readable, and organized code
###############################################
