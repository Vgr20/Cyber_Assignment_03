import requests
import concurrent.futures

url = "http://98.70.102.40:8080/api/auth/register"

def send_request(index):
    username = f"testuser{index}"
    password = "testpassword123"
    payload = {
        "username": username,
        "password": password,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(f"Response for {username}: ", response.status_code)
    print(f"Response Body for {username}: ", response.text)

# Use ThreadPoolExecutor for multithreading
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(send_request, range(200))