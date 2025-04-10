import requests

def api_call(username: str, password: str, url="http://98.70.102.40:8080/api/auth/secure-register"):
     response = requests.post(url, json={"username": username, "password": password})
     return response.status_code, response.text

first_response, first_body = api_call(username="testuser123", password="testpassword123")
print("First Response: ", first_response)
print("First Body: ", first_body)

second_response, second_body = api_call(username="testuser123", password="newpassword123")
print("Second Response: ", second_response)
print("Second Body: ", second_body)
