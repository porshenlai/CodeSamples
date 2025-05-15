import pandas

df = pandas.read_html("https://mopsov.twse.com.tw/server-java/t164sb01?step=1&CO_ID=2330&SYEAR=2024&SSEASON=4&REPORT_ID=C", encoding="big5")
with open("XBRL.json","w",encoding="utf8") as fo :
	fo.write(df[0].to_json(force_ascii=False))
	print("Results wrote to XBRL.json")
