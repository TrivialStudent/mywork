from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    contact = {"email": "lpurcell@nmhschool.org", "phone": 12345678910, "github": "trashbot7274"}
    return render_template("contact.html", contact=contact, )

@app.route("/about")
def about():
    hobies = ["Calisthenics", "Reading", "Programming"]
    return render_template("about.html", author="Lorcan", hobies=hobies)

app.run(debug=True)