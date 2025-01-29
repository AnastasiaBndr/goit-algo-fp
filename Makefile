.PHONY: install venv activate run_tests start build

venv:
	powershell -NoExit -Command "py -m venv .venv"

activate:
	powershell -NoExit -Command ".venv/Scripts/Activate.ps1"

leave:
	powershell -NoExit -Command "deactivate"

start:
	powershell -NoExit -Command "py main.py"

freeze:
	powershell -NoExit -Command "pip freeze | Out-File requirements.txt"