from flask import Flask, request
import requests

app = Flask(__name__)

# Simple HTML template (inline for demo)
form_html = """
    <h1>Weather App</h1>
    <form action="/weather" method="get">
        <label>Enter city:</label>
        <input type="text" name="city">
        <button type="submit">Get Weather</button>
    </form>
"""

@app.route("/")
def home():
    return form_html

@app.route("/weather")
def weather():
    city = request.args.get("city","boston")
    if not city:
        return "Please provide a city."
    url = "https://wttr.in/{}?format=3".format(city)  # free weather API
    response = requests.get(url)
    print(f"Response Headers: {response.headers}")
    print(f"Response Content: {response.content}")
    print(f"Response Text: {response.text}")   
    print(f"Response Request: {response.request}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response URL: {response.url}")

    html_content = f"<h1>Weather for {city}</h1><p>{response.text}</p><p>Debug: {city}</p><a href='/'>Back</a>"

    return html_content

if __name__ == "__main__":
    app.run(debug=True)