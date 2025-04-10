import requests

url = "http://98.70.102.40:8080/api/auth/login"

for i in range(100, 130):
    payload = {
        "username": f"testuser123",
        "password": f"testpassword{i}",
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(f"Attempt {i}: {response.status_code}")
    if response.status_code == 200:
        print("Success!")
        break
    elif response.status_code == 401:
        print("Unauthorized!")
    else:
        print("Unexpected response!")

    print(response.text)
    print("-" * 50)
