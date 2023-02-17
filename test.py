import requests

url = "https://sentim-api.herokuapp.com/api/v1/"

payload = {"text": "My day is going good. I might loose some money though."}
headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)