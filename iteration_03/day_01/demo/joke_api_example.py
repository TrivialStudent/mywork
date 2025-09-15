import requests

# https://official-joke-api.appspot.com/

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
data = response.json()

print(f"Here's a joke for you: {data['setup']}")
print(f"Punchline: {data['punchline']}")