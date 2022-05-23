import requests


def responseCheck(res):
    flag = -1
    if res >= 200 and res <= 299:
        print("Request Success")
        flag = 1
    elif res >= 300 and res <= 399:
        print("Redirection Message")
        flag = -1
    elif res >= 400 and res <= 499:
        print("Client error")
        flag = -1
    elif res >= 500 and res <= 599:
        print("Server error")
        flag = -1
    return flag


def auth(url="https://httpbin.org/basic-auth/unisys/mcp"):
    username = input("Enter Username:")
    password = input("Enter Password:")
    params = (username, password)
    try:
        r = requests.get(url, auth=params, timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.text)
        elif r.status_code == 401:
            print("Username or password is wrong")
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def redirect(url="https://httpbin.org/redirect-to"):
    payload = {"url": "https://github.com/"}
    try:
        r = requests.get(url, params=payload, timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.url)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def delay(url="https://httpbin.org/delay/4"):
    try:
        r = requests.get(url, timeout=3)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def post(url="https://httpbin.org/post"):
    try:
        payload = {"test1": "test1Value", "test2": "test2Value"}
        r = requests.post(url, data=payload, timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.text)
            r_dict = r.json()
            print(r_dict["form"])
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def get(url="https://httpbin.org/get", payload={}):
    try:
        payload = {"page": 2, "count": 25}
        r = requests.get(url, params=payload, timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.url, "\n")
            print(r.text)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def header(url="http://httpbin.org/headers"):
    try:
        payload = {"testheader": "header_value"}
        r = requests.get(url, headers=payload, timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.url, "\n")
            print(r.text)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def put(url="https://httpbin.org/put"):
    try:
        payload = {"test1": "test1Value", "test2": "test2Value"}
        r = requests.put(url, params=payload, timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.url, "\n")
            print(r.text)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def showip(url="https://httpbin.org/ip"):
    try:
        r = requests.get(url, timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.text)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


def ping_():
    try:
        r = requests.get("https://api-979bcd16.duosecurity.com/auth/v2/ping", timeout=3)
        if responseCheck(r.status_code) == 1:
            print(r.text)
    except requests.exceptions.ReadTimeout:
        print("Request Timed out")


# while True:
#     print("\n1.Auth\n2.Redirection\n3.Delay\n4.Post\n5.Get\n6.Header\n7.Put\n8.Show IP\n9.Exit\n")
#     ch = int(input("Enter your choice: "))
#     if ch == 1:
#         auth()
#     elif ch==2:
#         redirect()
#     elif ch == 3:
#         delay()
#     elif ch == 4:
#         post()
#     elif ch==5:
#         get()
#     elif ch==6:
#         header()
#     elif ch==7:
#         put()
#     elif ch==8:
#         showip()
#     elif ch==9:
#         break
#     else:
#         print("Enter correct choice")
