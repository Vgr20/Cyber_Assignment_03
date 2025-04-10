import time
import requests

url = "http://98.70.102.40:8080/api/auth/secure-register"
payload = {
    "username": "user1",
    "password": "admin@567"
}

for i in range(5):
    start = time.time()
    res = requests.post(url, json=payload)
    end = time.time()
    print(f"Attempt {i+1}: {end - start:.4f} seconds → {res.text}")

