SET logfile="C:\SwitchBackgrounds\batch.log"
@echo off
@echo Starting Script at %date% %time% >> %logfile%
"C:/Users/harri/AppData/Local/Programs/Python/Python38/python.exe" "C:/SwitchBackgrounds/switchBackgrounds.py"
@echo finished at %date% %time% >> %logfile%