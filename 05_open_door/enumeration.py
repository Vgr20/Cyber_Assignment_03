import requests

def api_call(pin: str, url="http://98.70.102.40:8080/api/smart-home/front-door/unlock"):
     response = requests.post(url, json={"pin": pin})
     return response.status_code, response.text

first_response, first_body = api_call(pin="1234")
print("First Response: ", first_response)
print("First Body: ", first_body)

second_response, second_body = api_call(pin="1234")
print("Second Response: ", second_response)
print("Second Body: ", second_body)

if first_body == second_body:
    print("Same response body detected.")