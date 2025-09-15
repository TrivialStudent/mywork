import requests

url = "https://api.nasa.gov/planetary/apod" # url for NASA planetary data api
params = {"api_key": "aFDopeewTYcb45medLtkipu6mHCdbFrv4L0017aT"}  # free demo key from NASA

response = requests.get(url, params)
data = response.json()

print("Title:", data["title"])
print("Date:", data["date"])
print("Explanation:", data["explanation"][:200] + "...")
print("Image URL:", data["url"])
