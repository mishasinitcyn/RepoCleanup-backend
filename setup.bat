@echo off

:: Create a virtual environment named 'venv'
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install the required packages from requirements.txt
pip install -r requirements.txt

echo Virtual environment setup complete and packages installed.

