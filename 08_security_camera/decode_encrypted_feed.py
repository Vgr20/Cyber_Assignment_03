import requests
import base64

def decode_feed(base_url, camera_id):
    url = f"{base_url}/api/smart-home/cameras/{camera_id}/feed"
    r = requests.get(url) # Adjust the endpoint as needed
    if r.status_code == 200: # Check if the response is valid and contains camera feed data
        data = r.json()
        encrypted_feed = data.get("encrypted_feed")
        if encrypted_feed:
            try:
                decoded_bytes = base64.b64decode(encrypted_feed) # Decode the base64 string
                print(f"[+] Decoded feed for {camera_id}: {decoded_bytes}")
            except Exception as e:
                print(f"[!] Could not decode feed: {e}")
        else:
            print("[-] 'encrypted_feed' key not found.")
    else:
        print(f"[-] HTTP {r.status_code} for camera {camera_id}")

if __name__ == "__main__":
    base_url = "http://98.70.102.40:8080"
    decode_feed(base_url, "camera123")