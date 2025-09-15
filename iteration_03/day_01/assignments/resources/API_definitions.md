# Flask Basics
* Definition
  * Flask is a lightweight Python web framework that lets you build web applications quickly.
* Use case
  * Turning Python scripts into web apps with routes, forms, and templates.
* Tip
  * Keep it simple at first: one file (app.py), one route (/), one template (index.html).

## APIs
* Definition
  * API = Application Programming Interface. It’s a contract that lets one program talk to another.
* Use case
  * Mobile and web apps (e.g., using Spotify’s API to pull your playlists).
* Tip
  * Think of APIs as waiters: you order (request), they bring food (response).

## Endpoints
* Definition
  * A specific URL where an API service lives (e.g., https://api.openweathermap.org/data/2.5/weather).
* Use case
  * Different endpoints provide different data (weather by city, weather by coordinates).
* Tip
  * Always check API docs for endpoints and required parameters.

## Authentication
* Definition
  * Proof you’re allowed to use the API (API key, OAuth token).
* Use case
  * NASA gives you a free API key to track usage. Spotify requires OAuth because data is private.
* Tip
  * Never hardcode private keys in code you push to GitHub. Store them in environment variables.

## JSON
* Definition
  * JavaScript Object Notation, a format for sending structured data (looks like Python dictionaries).
* Use case
  * Almost every modern API returns JSON.
* Tip
  * response.json() in Python turns JSON into a dict you can loop through.

## Routes
* Definition
  * URLs your Flask app responds to (@app.route("/")).
* Use case
  * /weather route displays weather data, /joke route displays a random joke.
* Tip
  * Start with one route, then add more.

## Templates

* Definition
  * HTML files that Flask fills in with data.
* Use case
  * Show weather data on a web page instead of printing to terminal.
* Tip
  * Put templates in a templates/ folder, and call them with render_template().

## Request/Response Cycle
* Definition
  * Client (browser) → sends request (GET or POST).
  * Server (Flask app) → processes → sends response (HTML, JSON, error).
*  Use case
   * Submitting a form → Flask calls API → Flask sends back a web page with results.
* Tip
  * Draw this cycle on the board as arrows: Browser → Flask → API → Flask → Browser.

## Resources for you (short + reliable)
* Flask official tutorial: https://flask.palletsprojects.com/en/latest/quickstart/
* RealPython guide to APIs: https://realpython.com/api-integration-in-python/
* MDN intro to APIs (student-friendly): https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction