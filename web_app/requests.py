import requests

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/1.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)