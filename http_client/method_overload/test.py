from urllib import request
import requests
import pytz
import datetime

d = datetime.datetime.now(pytz.timezone("utc"))
now = d.strftime("%a, %d %b %Y %H:%M:%S %z")
print(now)
r = requests.post(
    url="https://api-553eca93.duosecurity.com/auth/v2/preauth",
    headers={"X-Duo-Date": now, "X-Duo-Username": "MFAUSER"},
    auth=("DI70FEOY79HJPUF9Z36X", "iWD5gLj2ilk064FFGt5uFt61RO40EVYe9SS27vaV"),
)

print(r.text)
