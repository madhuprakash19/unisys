import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

course = [
    {"id": 1, "name": "Lakshana"},
    {"id": 2, "name": "Madhu"},
    {"id": 3, "name": "Nikitha"},
    {"id": 4, "name": "Laisha"},
]
headers = {
    "Content-Type": "application/json",
    "accept": "application/json",
}
res = requests.post(
    "https://127.0.0.1:5000/post", json=course, verify=False, headers=headers
)
print("response from server:", res.text)
dictFromServer = res.json()
print(dictFromServer)
