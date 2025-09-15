# Day Activity Plan: Build a Flask App with a Public API and Push to GitHub

## Objective
By the end of the day, students will:
1. Create a new GitHub repository.
2. Set up a basic Flask app.
3. Fetch data from a free public API.
4. Push their project to GitHub.

---

## Resources
- **GitHub:** https://github.com/  
- **Flask Documentation:** https://flask.palletsprojects.com/  
- **Free Public APIs:**  
  - https://github.com/public-apis/public-apis  
  - Examples:  
    - Cat Facts: `https://catfact.ninja/fact`  
    - Random Joke: `https://official-joke-api.appspot.com/random_joke`  
    - NASA Picture of the Day: `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY`  

---

## Part 1: Create a New GitHub Repository

1. Go to [GitHub](https://github.com/) and log in (or create an account).  
2. Click **New repository**.  
3. Give it a name (e.g., `my-flask-api-app`).  
4. Choose **Public** and **Initialize with a README**.  
5. Click **Create repository**.  

## Part 2: Set Up Your Project Locally

### 1. Clone Your Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Set Up Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Flask and Requests
```bash
pip install Flask requests
```

### 4. Create Basic Flask App
1. Create new file called `app.py`
2. Add Following Code

```python
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Flask API App!</h1>"

@app.route("/get-fact")
def get_fact():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
```

## Assignment
1. Use a different API from https://github.com/public-apis/public-apis 
2. Add multiple routes and use query parameters in your application
3. Utilize a form which will direct user to new route with information that was submitted by user.
4. Push to github and submit URL to repo into Canvas assignment