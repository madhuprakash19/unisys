from urllib import response
import requests
import os

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def showall():
    response = requests.get("https://127.0.0.1:5000/app/api/course/all", timeout=3,verify=False)
    print(response.text)


def single():
    id1 = int(input("Enter id to be searched: "))
    getthis = {"id": id1}
    response = requests.get(
        "https://127.0.0.1:5000/showit/", timeout=3, params=getthis, verify=False
    )
    print("/n" + response.text)


def append():
    id = int(input("Enter the id you want to add: "))
    name = input("Enter the name you want to add: ")
    d = {"id": id, "name": name}
    response = requests.get(
        "https://127.0.0.1:5000/append/", timeout=3, params=d, verify=False
    )
    print("\n" + response.text)


def update():
    id = int(input("Enter the id you want to update: "))
    name = input("Enter the name you want to update: ")
    d = {"id": id, "name": name}
    response = requests.get(
        "https://127.0.0.1:5000/update/", timeout=3, params=d, verify=False
    )
    print("\n" + response.text)
    
while True:
    print("1.Display ALL\n2.Display one Id\n3.Append\n4.Update\n5.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        showall()
    elif ch == 2:
        single()
    elif ch == 3:
        append()
    elif ch == 4:
        update()
    else:
        break
