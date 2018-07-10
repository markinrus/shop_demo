import requests
response = requests.get("https://httpbin.org/get")
print (response.content)
response.json()
response.headers
response.headers.get("Server")