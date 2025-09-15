# Day 1: APIs & Flask Basics

## API References

- **Cat Facts API**  
  [https://catfact.ninja/](https://catfact.ninja/)  

- **Random Joke API**  
  [https://official-joke-api.appspot.com/](https://official-joke-api.appspot.com/)  

- **NASA Picture of the Day API**  
  [https://api.nasa.gov/](https://api.nasa.gov/)  

---

## What Happens When You Run `requests.get(url)`

1. Your Python program sends an **HTTP GET request** to the URL you provided.
2. The server at that URL receives your request and sends back a **response**.
3. The response contains:
   - **Headers** (metadata about the response, e.g., content type)
   - **Body** (the actual data, usually JSON, plain text, or HTML)
   - **Status code** (indicates success, error, or redirection)

**Example:**
```python
import requests
response = requests.get("https://catfact.ninja/fact")
print(response.status_code)  # 200 = success
print(response.text)         # raw response content
```

## Why Do We Call `response.json()`
1. Terminal Based Apps
   * Print API data directly using print()
   * Example: random joke printed in the console
   * Printing to the terminal is only visible to the developer.
2. Web Based Apps (Flask)
   * Use Flask to define a route that fetches the API data.
   * Return HTML that displays the data in a browser.
   * Showing data in a webpage allows users to interact with your app.

**Example:**
```python
@app.route("/catfact")
def cat_fact():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    return f"<h1>Cat Fact</h1><p>{data['fact']}</p>"
```

## API Request / Response Relationship
* Client: The program making the request (your Python script or browser).
* Server: The program hosting the API, which receives requests and sends responses.
* Request: Includes method (GET, POST, etc.), URL, headers, and optional body.
* Response: Includes status code, headers, and body (data in JSON, text, etc.).

`Client sends request → Server processes → Server sends response → Client parses response`

### **Common HTTP Status Codes**
Status :: Meaning

`200` :: OK – request succeeded.  
`201` :: Created – new resource created.  
`400` :: Bad Request – request invalid.  
`401` :: Unauthorized – API key missing or invalid.  
`403` :: Forbidden – not allowed.  
`404` :: Not Found – endpoint doesn’t exist.  
`500` :: Internal Server Error – server problem.  

---

## Notes For When Using `response`

1. Check `status_code` before using response.json()
   * Some requests fail. Calling `.json()` on a non-JSON response will throw an error.
2. Check `Content-Type` header (response.headers["Content-Type"])
   * Make sure it’s `application/json` before calling `.json()`
   * If it’s `text/plain` or `text/html`, use `response.text` instead.
3. Rate Limits
   * Some APIs limit how many requests you can make per minute or per day.
4. Authentication / API Keys
   * Many APIs require keys or tokens. Never share private keys in public code.