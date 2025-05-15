import requests
from time import time
from json import dump

StockID="2330"
Date="20250101"
TS=int(time()*1000)

# https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20250515&stockNo=2330&response=csv
url = "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date={0:s}&stockNo={1:s}&response=json&_={2:d}".format(Date,StockID,TS)
r = requests.get(url)
with open("StockHistory.json","w",encoding="utf8") as fo :
	dump(r.json(),fo,ensure_ascii=False)
	print("Results wrote to StockHistory.json")
