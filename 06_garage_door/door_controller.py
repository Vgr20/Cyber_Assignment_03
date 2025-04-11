import requests

url = "http://98.70.102.40:8080/api/smart-home/garage/toggle"

payload = {
    "command": "open",
    "password": "testpassword123",
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)