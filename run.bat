@echo off

REM Check if Python 3.7 is installed
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python 3.7 is already installed.
) else (
    echo Installing Python 3.7...
    choco install python --version=3.7 -y

    REM Add Python to the PATH environment variable
    setx PATH "%PATH%;C:\Python37" /M

    REM Close and reopen the command prompt to apply PATH changes
    echo Please close and reopen the command prompt to proceed.
    pause
    exit
)

:reopen
REM Check if main.py exists
if exist main.py (
    echo main.py already exists.
) else (
    REM Download main.py
    echo Downloading main.py...
    curl -o main.py https://raw.githubusercontent.com/Abhijith14/bulk-bg-remover/master/main.py
    powershell -command "& {Invoke-WebRequest -Uri https://github.com/alshukairi/public/raw/main/LAV_Weight/LAV_weights.zip.000 -OutFile LAV_weights.zip.000}"
    https://github.com/Abhijith14/public/raw/master/main.py
)

REM Check if rembg is installed
pip show rembg >nul 2>&1
if %errorlevel% equ 0 (
    echo rembg is already installed.
) else (
    REM Run pip install rembg
    echo Installing rembg...
    pip install rembg
)

REM Check if input folder exists
if not exist input (
    echo Creating input folder...
    mkdir input
    echo Please add images to the input folder and run this script again.
)

REM Run python main.py
echo Running main.py...
python main.py

pause
exit
