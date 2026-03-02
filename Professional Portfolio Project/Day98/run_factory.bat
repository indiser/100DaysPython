@echo off
echo Waking up the Viral Brainrot Factory...

:: 1. Force the system to navigate to your exact project folder first
cd /d "C:\Users\ranab\OneDrive\Desktop\AutoContent"

:: 2. The Production Loop (Runs exactly 3 times)
FOR /L %%A IN (1,1,3) DO (
    echo.
    echo ========================================
    echo COMMENCING FACTORY RUN: %%A OF 3
    echo ========================================
    "C:\Users\ranab\AppData\Local\Programs\Python\Python313\python.exe" main_pipeline.py
)

echo Pipeline execution complete. 
echo Running inventory check and alert system...

:: 3. Run your custom email alert microservice ONCE at the end
"C:\Users\ranab\AppData\Local\Programs\Python\Python313\python.exe" reminder.py

echo Factory shutdown sequence complete.
pause