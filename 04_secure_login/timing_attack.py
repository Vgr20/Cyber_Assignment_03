import time
import requests

url = "http://98.70.102.40:8080/api/auth/secure-login"

start = time.time()
response = requests.post(url, json={"username": "testuser123", "password": "testpassword123"})
print("Correct user, correct password:", time.time() - start)

start = time.time()
response = requests.post(url, json={"username": "testuser123", "password": "testpassword12345"})
print("Correct user, wrong password:", time.time() - start)

start = time.time()
requests.post(url, json={"username": "user1", "password": "admin@567"})
print("Correct user, correct password:", time.time() - start)

start = time.time()
requests.post(url, json={"username": "fakeUser1", "password": "anything"})
print("Wrong user:", time.time() - start)


start = time.time()
requests.post(url, json={"username": "fakeUser2", "password": "something"})
print("Wrong user:", time.time() - start)