import requests

# endpoint="https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"


get_response=requests.post(endpoint, json={"title":"The title", "content":"Hello World"}) 
# emmulate HTTP request
# print(get_response.text)  #print raw text response
# print(get_response.status_code)

# HTTP Request ->HTML
# REST API HTTP Request -> JSON
print(get_response.json())
