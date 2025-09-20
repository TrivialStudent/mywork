# Thursday, September 18, 2025

## 1. Complete Iteration 03 Day 01 Work Shop
* Create Flask app with home form home page
* Should have total of 3 routes (Home + 2 more)
* If applicable to API, use query parameters

## 2. Python Bonus Challenge: “Random User Bio Generator”

### The Task

Build a Flask mini-app that generates a random “user bio” when you visit a route in your browser.

### Requirements

1. Create a Python class User in a separate file (user.py) with attributes:
   * name
   * age
   * hobby

2. In your main Flask app (app.py):

   * Import the User class.
   * Create a list of sample data for names, ages, and hobbies.
   * Use Python’s random module to generate a new user when someone visits /user.

   * When a new User is created:
      * Convert the user object to a dictionary.
      * Dump the dictionary into JSON format.
      * Save it to a file (e.g., user.json).
      * Return the JSON data to the browser.
    * Add another route /show that:
      * Reads the user.json file.
      * Loads the JSON data back into Python.
      * Displays the user’s info in a simple HTML template.

### Example Expected Behavior

1. Go to /user → App creates a random user like:  

    ```json
    {
    "name": "Alice",
    "age": 27,
    "hobby": "painting"
    }
    ```

2. Go to /show → You see:  

    ```python
    Name: Alice
    Age: 27
    Hobby: painting
    ```

3. Stretch Goals (in case students finish early):

   * Add more attributes (e.g., “favorite animal,” “lucky number”).
   * Generate multiple random users at once and save them to a JSON list.
   * Add a form on the home page that asks: How many random users do you want?