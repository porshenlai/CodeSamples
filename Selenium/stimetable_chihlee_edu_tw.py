from sys import exit
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

browser = webdriver.Chrome()

browser.get('https://stimetable.chihlee.edu.tw')
#browser.find_element(By.CSS_SELECTOR,"")
print(browser.current_url)

try:
	while True :
		element = WebDriverWait(browser, 86400).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "#btnAbsData"))
		)

		with open("stimetable_chihlee_edu_tw.js","r",encoding="utf8") as fo :
			browser.execute_script(fo.read());

		element = WebDriverWait(browser, 86400).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "#gvCourseList"))
		)
except Exception as x :
	print("Exception:",type(x))
