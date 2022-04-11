from urllib import response
import requests


def showall():
    response = requests.get("http://127.0.0.1:5000/app/api/course/all", timeout=3)
    print(response.text)


def single():
    id1 = int(input("Enter id to be searched"))
    getthis = {"id": id1}
    response = requests.get("http://127.0.0.1:5000/showit/", timeout=3, params=getthis)
    print("/n" + response.text)


while True:
    print("1.Display\n2.Single")
    ch1 = int(input("Enter ur choice"))
    if ch1 == 1:
        showall()
    elif ch1 == 2:
        single()
