from flask import Flask, request, render_template, jsonify
import requests
app = Flask(__name__)

form_html = """
    <form method="POST">
    <input name="domain">
    <input type="submit">
    </form>"""

params = {"X-Api-Key": "LkIdYNAWQCqSs4iciDf7kA==JDcU456DxgbhiMTy"}


@app.route("/")
def home():
    return f"WELCOME TO MY WEBSITE.\nCheck out /get-fact to get a fact, /get-quote to get a quote, or /get-domain to enter domain and get WHOIS data"

@app.route("/get-fact")
def get_fact():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    print("Random Cat Fact:", data["fact"])
    return data
@app.route("/get-quote")
def get_quote():
    response = requests.get("https://api.api-ninjas.com/v1/quotes", params)
    data = response.json()
    return jsonify(data)


@app.route("/get-domain", methods=["GET", "POST"])
def _form():
    if request.method == "POST":
        domain = request.form.get("domain", "google.com")
        response = requests.get(f"https://api.api-ninjas.com/v1/whois?domain={domain}", params)
        data = response.json()
        return jsonify(data)
    return form_html

if __name__ == "__main__":
    app.run(debug=True)