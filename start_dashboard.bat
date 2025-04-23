@echo off
echo Setting up virtual environment...
python -m venv venv
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Launching the dashboard...
python backend\app.py

pause
