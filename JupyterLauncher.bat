@echo off

REM cd <change cwd to notebook-containing folder>

set env=base
set root=C:\Users\Mak\Anaconda3

call %root%\Scripts\activate.bat %env%
call jupyter lab

REM uncomment line below to keep terminal window open after notebook server shutdown (to see notebook error messages etc.)
REM pause