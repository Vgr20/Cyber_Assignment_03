import requests

url = "http://98.70.102.40:8080/api/auth/register"

weak_passwords = [ "123", "password", "123456", "123456789", "qwerty", "abc123", "111111", "12345678", "12345", "1234567", "sunshine", "iloveyou", "princess", "admin", "welcome", "666666", "abc123456"]

for pwd in weak_passwords:
    payload = {
        "username": "testuser123",
        "password": pwd,
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(f"Testing password: {pwd}")
    print("Response: ", response.status_code)
    print("Response Body: ", response.text)
    print("-" * 50)

