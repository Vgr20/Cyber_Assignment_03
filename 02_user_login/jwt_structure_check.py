import jwt
import base64

token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0dXNlcjEyMyIsImV4cCI6MTc0NDMwNDgyOH0.BBPCjrcU58VfQbQJRXhvxsEBNF-hZ3_QWkBDwEBgXrU"
header, payload, signature = token.split('.')

# Decode the header and payload
decoded_header = base64.urlsafe_b64decode(header + '==')
decoded_payload = base64.urlsafe_b64decode(payload + '==')

print("Decoded Header:", decoded_header.decode())
print("Decoded Payload:", decoded_payload.decode())