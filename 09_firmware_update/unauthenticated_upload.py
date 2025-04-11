import requests
import json

def upload_dummy_firmware():
    url = "http://98.70.102.40:8080/api/smart-home/firmware/upload"
    payload = {
        "firmware": "dummyFirmwareData"  # Plain string pretending to be encrypted firmware
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("[*] Status Code:", response.status_code)
    print("[*] Response Body:", response.text)

upload_dummy_firmware()
