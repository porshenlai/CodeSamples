import requests

url = "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20250305&type=17&response=json"
r = requests.get(url)
print(r.json())
