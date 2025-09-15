import requests

# https://catfact.ninja/

url = "https://catfact.ninja/fact"
response = requests.get(url)
data = response.json()

print("Random Cat Fact:", data["fact"])
