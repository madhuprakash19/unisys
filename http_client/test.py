import requests

a = requests.get("https://api-979bcd16.duosecurity.com/auth/v2/ping")
print(a.text)
