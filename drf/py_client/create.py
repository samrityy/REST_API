import requests
endpoint="http://localhost:8000/api/products/"


data ={
    "title":"This field ",
    "price":322.2
}
get_response =requests.post(endpoint,json=data)
print(get_response.json())