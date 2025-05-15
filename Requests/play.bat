powershell -c ..\bin\install.ps1
if exist "DailyPrice.py" (
	__pyenv__\python.exe DailyPrice.py
)
if exist "StockHistory.py" (
	__pyenv__\python.exe StockHistory.py
)
if exist "XBRL.py" (
	__pyenv__\python.exe XBRL.py
)
pause -1
