from flask import Flask, request, jsonify
from json2html import *

import json

app = Flask(__name__)



form_html = form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bio App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f7fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .form-container {
            background: white;
            padding: 2rem 2.5rem;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            width: 320px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 1.5rem;
        }
        label {
            display: block;
            margin-top: 1rem;
            font-weight: 600;
            color: #444;
        }
        input {
            width: 100%;
            padding: 0.6rem;
            margin-top: 0.4rem;
            border: 1px solid #ccc;
            border-radius: 6px;
            transition: border-color 0.2s ease;
        }
        input:focus {
            outline: none;
            border-color: #007bff;
        }
        button {
            width: 100%;
            padding: 0.7rem;
            margin-top: 1.5rem;
            border: none;
            border-radius: 6px;
            background-color: #007bff;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.2s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Bio App</h1>
        <form action="/user" method="get">
            <label for="name">Enter Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="age">Enter Age:</label>
            <input type="number" id="age" name="age" required>
            
            <label for="hobby">Enter Hobby:</label>
            <input type="text" id="hobby" name="hobby">
            
            <button type="submit">Show Bio</button>
        </form>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    return form_html
@app.route("/user")
def user():
    name = request.args.get("name", "NO_NAME")
    age = request.args.get("age", "NO_AGE")
    hobby = request.args.get("hobby", "NO_HOBBY")
    if not name:
        return "Please enter your name"
    user_dict = {"name": name, "age": age, "hobby": hobby}
    save_data(user_dict)
    return jsonify(user_dict)


def save_data(new_user):
    try:
        with open('data.json', 'r') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    if isinstance(users, dict):
        users = [users]

    users.append(new_user)

    with open('data.json', 'w') as f:
        json.dump(users, f, indent=4)



@app.route("/show")
def show():
    with open('data.json', 'r') as file:
        data = json.load(file)

    table = json2html.convert(json=data)

    return f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    padding: 2rem;
                    background: #f5f7fa;
                }}
                .container {{
                    background: white;
                    padding: 2rem;
                    border-radius: 12px;
                    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
                    max-width: 600px;
                    margin: auto;
                }}
                h1 {{
                    text-align: center;
                    color: #333;
                }}
                .btn {{
                    display: block;
                    width: 200px;
                    margin: 2rem auto 0;
                    padding: 0.8rem;
                    text-align: center;
                    background-color: #007bff;
                    color: white;
                    border-radius: 6px;
                    text-decoration: none;
                    font-weight: bold;
                    transition: background 0.2s ease;
                }}
                .btn:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>All Users</h1>
                {table}
                <a href="/" class="btn">Return Home</a>
            </div>
        </body>
        </html>
        """


if __name__ == "__main__":
    app.run(debug=True)
