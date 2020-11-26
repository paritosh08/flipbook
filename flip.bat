@echo off

IF "%2" == "-o" (goto check2) else (goto wrongArg)
:check2
if "%~3" == "" (goto wrongArg) else (goto runProg)

:runProg
python code.py %1 %3
echo Done
goto comExit

:wrongArg
echo Wrong arguments
goto comExit

:comExit