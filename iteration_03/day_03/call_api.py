import requests

# Use requests package to call your api address http://127.0.0.1:5000/api/joke to display a funny joke


url = "http://127.0.0.1:5000/api/jokes/Because"

request = requests.get(url)

data = request.json()

print(data)