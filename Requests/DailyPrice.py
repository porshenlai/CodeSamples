import requests
from json import dump

url = "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20250305&type=17&response=json"
r = requests.get(url)
with open("DailyPrice.json","w",encoding="utf8") as fo :
	dump(r.json(),fo,ensure_ascii=False)
	print("Results wrote to DailyPrice.json")
