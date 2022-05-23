import requests


class httpclient:
    def responseCheck(self, res):
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

    def get(self, url, params, header, pdata):
        try:
            r = requests.post(url, auth=params, headers=header, data=pdata, timeout=3)
            if self.responseCheck(r.status_code) == 1:
                print(r.text)
            elif r.status_code == 401:
                print("Username or password is wrong")
        except requests.exceptions.ReadTimeout:
            print("Request Timed out")

    def post(self, url, header, pdata):
        try:
            r = requests.post(url, headers=header, data=pdata, timeout=3)
            if self.responseCheck(r.status_code) == 1:
                print(r.text)
        except requests.exceptions.ReadTimeout:
            print("Request Timed out")

    def post(self, url):
        try:
            r = requests.get(url, timeout=3)
            if self.responseCheck(r.status_code) == 1:
                print(r.text)
        except requests.exceptions.ReadTimeout:
            print("Request Timed out")

    def get(self, url):
        try:
            r = requests.get(url, timeout=3)
            if self.responseCheck(r.status_code) == 1:
                print(r.text)
        except requests.exceptions.ReadTimeout:
            print("Request Timed out")


def main():
    test1 = httpclient()
    # ok = {"test1": "test1Value", "test2": "test2Value"}
    # test1.post("https://httpbin.org/post", {}, ok)
    test1.get("https://httpbin.org/ip")


if __name__ == "__main__":
    main()
