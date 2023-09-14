import requests

headers={'Authorization':
     'Bearer f1642bd73ff78f625db2a8b200372b05872c30bc'   }
endpoint="http://localhost:8000/api/products/"


data ={
    "title":"This field ",
    "price":322.2
}
get_response =requests.post(endpoint,json=data , headers=headers) 
print(get_response.json())