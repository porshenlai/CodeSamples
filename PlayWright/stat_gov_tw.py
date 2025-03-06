from os import path as Path
from playwright.sync_api import sync_playwright, Playwright

Conf={
	"URL":"https://www.stat.gov.tw/",
	"ScreenShot":"screenshot.png"
}

def run(playwright: Playwright):
	chromium = playwright.chromium # or "firefox" or "webkit".
	browser = chromium.launch()
	context = browser.new_context(
		user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
	)
	page = context.new_page()
	def on_log (msg) :
		if msg.text.startswith("RESULT=") :
			print(msg.text)
			with open("result.json","w") as fo :
				fo.write(msg.text.replace("RESULT= ",""))
		else :
			print("LOG:",msg.text)
	page.on("console", on_log)

	page.goto(Conf["URL"])

	#page.locator('a[title="經濟成長率"]').click()
	page.get_by_role("link", name="經濟成長率", exact=True).click()
	if "ScreenShot" in Conf :
		page.screenshot(path=Conf["ScreenShot"])
	#page.evaluate("console.log('Hello World');")
	with open(Path.join(Path.dirname(__file__),"stat_gov_tw.js"),"r",encoding="utf8") as fo :
		page.evaluate(fo.read())
	browser.close()

with sync_playwright() as playwright:
	run(playwright)
