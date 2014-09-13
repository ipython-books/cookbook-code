REM ## This is needed for setenv.cmd later
setlocal EnableDelayedExpansion
REM ## STORE OLD DIR
set olddir=%cd%

REM ## DETERMINE SDK DIR
SET SDKREG=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft SDKs\Windows\v7.0
SET SDKDIRQUERY=reg query "%SDKREG%" /v InstallationFolder
FOR /F "tokens=2* delims= " %%A IN ('%SDKDIRQUERY%') DO SET SDKDIR=%%B
REM Tab followed by Space ^^^^^^

REM ## STARTUP COMPILE ENVIRONMENT
call "%SDKDIR%\bin\setenv.cmd" /x64 /release

REM ## RESET DIRECTORY
chdir /d %olddir%
set DISTUTILS_USE_SDK=1

REM ## YOUR COMMANDS GO HERE
ipython notebook --profile=cookbook
