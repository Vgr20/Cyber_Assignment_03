import base64

original = "Temp:72°F, Usage:4kW"
hash = "BjJbADy+1CU8mINdo4XE7A=="
decoded_hash = base64.b64decode(hash)

print("[+] Decoded Hash (raw bytes):", decoded_hash)