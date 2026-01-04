@echo off
echo Installing requirements...
pip install -r requirements.txt
pip install pyinstaller

echo.
echo Starting Build!
pyinstaller --onefile --windowed --name=AudioFix --workpath=%TEMP%\audiofix_build --distpath=./ --specpath=%TEMP%\audiofix_build audiofix.py
echo.
echo Build complete! EXE is located at %cd%!

set /p startup="Copy to EXE to startup folder? (y/n): "
if /i "%startup%"=="y" (
    copy dist\AudioFix.exe "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\AudioFix.exe"
    echo Successfully copied to startup folder!
) else (
    echo Skipped startup copy.
)
echo.
pause