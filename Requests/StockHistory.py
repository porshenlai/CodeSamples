import requests
from time import time

StockID="2330"
Date="20250201"
TS=int(time()*1000)

url = "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date={0:s}&stockNo={1:s}&response=json&_={2:d}".format(Date,StockID,TS)
r = requests.get(url)
print(r.json())
