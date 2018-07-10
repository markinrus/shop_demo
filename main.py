import requests
  
result = requests.get("https://bluzir.me/python/course")
print(result.text)