import requests

url = "http://98.70.102.40:8080/api/auth/register"

payload = {
    "username": "testuser123",
    "password": "testpassword123",
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)