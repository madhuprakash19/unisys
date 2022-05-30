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


def get(url="https://httpbin.org/get"):
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