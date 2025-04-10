import requests

url = "http://98.70.102.40:8080/api/auth/secure-register"

payload = {
    "username": "testuser123",
    "password": "testpassword123",
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
status = response.status_code
response_text = response.text
print(status)   
print(response_text)

