from sys import exit
from os import path
from time import sleep
from json import dump

from pygetwindow import getAllTitles, getWindowsWithTitle
from pyautogui import click, screenshot, locateOnScreen, hotkey, press, write, moveTo

def findTitle(key) :
	wnd=[ t for t in getAllTitles() if t.find(key) >= 0 ]
	return wnd[0] if len(wnd) > 0 else None

def waitForView(url,to=30) :
	for s in range(0,to) :
		try :
			moveTo(10,10)
			r = locateOnScreen(url, grayscale=True, confidence=0.9)
			return r
		except Exception as x :
			print(f"Exception: {url}",x,type(x))
			sleep(1)

def hit_keys (keys) :
	for key in keys :
		if type(key) == tuple :
			hotkey(*key)
		else :
			press(key)
		sleep(0.5)

from ctypes import c_void_p, c_char_p, windll
kernel32 = windll.kernel32
kernel32.GlobalLock.argtypes = [c_void_p]
kernel32.GlobalLock.restype = c_void_p
kernel32.GlobalUnlock.argtypes = [c_void_p]
user32 = windll.user32
user32.GetClipboardData.restype = c_void_p
def get_clipboard_text(CF_TEXT=1):
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            return value.replace(b"\r",b"\n").decode('ansi')
    finally:
        user32.CloseClipboard()

def decodeTable (s) :
	s=s.split("\n")
	return {
		"C":s[0].split("\t"),
		"D":[ line.split("\t") for line in s[1:] if line ]
	}

WTitle=findTitle("CMoney(")
Wnd=None

if not WTitle :
	hotkey('win','r')
	write(path.join(path.dirname(__file__),"C:\\Windows\\Notepad.exe\n"))
	#screenshot("sample.png")
	for s in range(0,30) :
		WTitle=findTitle("CMoney(")
		if WTitle : break;
		sleep(1)

print(f"get window: {WTitle}")
while not Wnd :
	Wnd=getWindowsWithTitle(WTitle)[0]
	sleep(1)

Wnd.activate()
Wnd.maximize()

try :
	waitForView("kbar.png",30);
	sleep(3)
	click(10,10)
	hit_keys([("alt","q"),"left","right","right","enter"]);
	for s in range(0,20) :
		waitForView("wait.png",3)
		try :
			print("Wait")
			locateOnScreen("wait.png", grayscale=True, confidence=0.9)
			sleep(1)
		except :
			break;

	print("Ready")
	Tasks=[("3380","20241014-20241018"),("0050","20241014-20241018")]
	for (target, duration) in Tasks :
		rect=waitForView("target.png",10)
		click(x=rect.left-rect.width,y=rect.top+rect.height//2)

		write(target)
		press("tab")
		write(duration)
		press("enter")

		hotkey("ctrl","a")
		hotkey("ctrl","c")
		sleep(3)
		result=get_clipboard_text()
		print(f"{target} @ {duration}")
		with open(f"{target}_{duration}.json","w",encoding="utf8") as fo :
			dump(decodeTable(result),fo,ensure_ascii=False);
		sleep(1)
except Exception as x :
	print("Exception:",x,type(x));
	screenshot("exception.png")

#Wnd.minimize();
Wnd.close();
