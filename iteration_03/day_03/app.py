from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

jokes = [
    {"setup": "Why did the scarecrow win an award?", "punchline": "Because he was outstanding in his field!"},
    {"setup": "Why don’t skeletons fight each other?", "punchline": "They don’t have the guts."},
    {"setup": "What do you call fake spaghetti?", "punchline": "An impasta."},
    {"setup": "Why did the bicycle fall over?", "punchline": "Because it was two-tired."},
    {"setup": "Why did the math book look sad?", "punchline": "Because it had too many problems."},
    {"setup": "Why don’t scientists trust atoms?", "punchline": "Because they make up everything."},
    {"setup": "Why did the coffee file a police report?", "punchline": "It got mugged."},
    {"setup": "Why was the computer cold?", "punchline": "It left its Windows open."},
    {"setup": "Why did the tomato turn red?", "punchline": "Because it saw the salad dressing!"},
    {"setup": "Why did the cookie go to the hospital?", "punchline": "Because he felt crummy."},
    {"setup": "Why don’t oysters share their pearls?", "punchline": "Because they’re shellfish."},
    {"setup": "Why did the skeleton go to the party alone?", "punchline": "He had no body to go with."},
    {"setup": "Why did the golfer bring two pairs of pants?", "punchline": "In case he got a hole in one."},
    {"setup": "Why did the smartphone need glasses?", "punchline": "It lost its contacts."},
]

@app.route("/")
def home():
    html_content = """
        <h1>Joke API</h1>
        <p>Be sure to visit http://127.0.0.1:5000/api/joke for a funny joke!</p>
        <p>Be sure to visit http://127.0.0.1:5000/api/jokes/2 for 2 funny jokes!</p>
    """
    return html_content

@app.route("/api/joke")
def get_joke():
    return jsonify(random.choice(jokes))


@app.route("/api/jokes/<int:num>")
def get_jokes(num):
    results = []
    for _ in range(num):
        results.append(random.choice(jokes))
    return jsonify(results)

@app.route("/api/jokes/<occurence>")
def get_joke_word(occurence):
    return jsonify([x for x in jokes if occurence.lower() in x['punchline'].lower()])

###############################################################################
# Now you need to add a route parameter! Think about how we can do this using #
# our python logic after I show you how to insert a route parameter.          #
###############################################################################

if __name__ == "__main__":
    app.run()