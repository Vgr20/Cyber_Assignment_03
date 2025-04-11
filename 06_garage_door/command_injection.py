import requests

def api_call(command: str, url = "http://98.70.102.40:8080/api/smart-home/garage/toggle"):
     response = requests.post(url, json={"command": command})
     return response.status_code, response.text

first_response, first_body = api_call(command="open")
print("First Response: ", first_response)
print("First Body: ", first_body)

second_response, second_body = api_call(command="open")
print("Second Response: ", second_response)
print("Second Body: ", second_body)

third_response, third_body = api_call(command="echo open")
print("Third Response: ", third_response)
print("Third Body: ", third_body)

if first_body == second_body == third_body:
    print("Command injection detected.")
else:
    print("No command injection detected.")