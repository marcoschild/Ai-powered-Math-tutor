import requests

url = "http://127.0.0.1:5000/solve"
data = {"problem": "x**2 - 4"}  # Example problem

response = requests.post(url, json=data)
print(response.json())  # Print the API response
