@echo off
mode con cols=100 lines=50 &color 0a
title CLASSIFIED COMPUTER INIT MODULE 1
:m
cls
set /a empty = empty + 1
set BAR=%BAR%Û
echo.
echo.
echo              Chargement ADMINISTRATOR COMPUTER
echo.
echo              %BAR%                             
echo.
if %empty%==37 goto endbar
@ping localhost -n 1 >nul
echo          %random% %random% %random% %random% %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo  %random%   %random%%random% %random%    %random%   %random% %random% %random%   %random%
echo    %random%  %random%   %random% %random%        %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%  %random% %random% %random%   %random%
echo %random%   %random%   %random% %random%    %random%     %random%     %random% %random%
echo  %random%   %random%   %random% %random%    %random%   %random% %random% %random%   %random%
echo          %random% %random% %random% %random% %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo  %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo    %random%  %random%   %random% %random%        %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%  %random% %random% %random%   %random%
echo %random%   %random%   %random%%random%    %random%     %random%     %random% %random%
echo  %random%   %random%   %random% %random%    %random%   %random% %random% %random%   %random%
echo          %random% %random% %random% %random% %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo  %random%   %random% %random% %random%    %random%   %random% %random% %random%   %random%
echo    %random%  %random%   %random% %random%         %random% %random% %random%   %random%
echo      %random%   %random% %random% %random%    %random%  %random% %random% %random%   %random%
echo %random%   %random%   %random% %random%    %random%     %random%     %random% %random%
echo  %random%   %random%   %random% %random%    %random%   %random% %random% %random%   %random%
goto m
:endbar

color a
set /a mat=1
set /a var=1
:rand
set /a m="%random%%%27"
if "%m%" == "0" set matrix%mat%= 
if "%m%" == "1" set matrix%mat%=a
if "%m%" == "2" set matrix%mat%=b
if "%m%" == "3" set matrix%mat%=c
if "%m%" == "4" set matrix%mat%=d
if "%m%" == "5" set matrix%mat%=e
if "%m%" == "6" set matrix%mat%=f
if "%m%" == "7" set matrix%mat%=g
if "%m%" == "8" set matrix%mat%=h
if "%m%" == "9" set matrix%mat%=i
if "%m%" == "10" set matrix%mat%=j
if "%m%" == "11" set matrix%mat%=k
if "%m%" == "12" set matrix%mat%=l
if "%m%" == "13" set matrix%mat%=m
if "%m%" == "14" set matrix%mat%=n
if "%m%" == "15" set matrix%mat%=o
if "%m%" == "16" set matrix%mat%=p
if "%m%" == "17" set matrix%mat%=q
if "%m%" == "18" set matrix%mat%=r
if "%m%" == "19" set matrix%mat%=s
if "%m%" == "20" set matrix%mat%=t
if "%m%" == "21" set matrix%mat%=u
if "%m%" == "22" set matrix%mat%=v
if "%m%" == "23" set matrix%mat%=w
if "%m%" == "24" set matrix%mat%=x
if "%m%" == "25" set matrix%mat%=y
if "%m%" == "26" set matrix%mat%=z
if "%mat%" == "12" goto echo
set /a mat=%mat%+1
set /a var=%var%+1
if %var% == 1000 goto coucou


goto rand
:echo
echo %matrix1% %matrix2%  %matrix3%  %matrix4% %matrix5%  %matrix6% %matrix7% %matrix8%  %matrix9%  %matrix10% %matrix11% %matrix5% %matrix1% %matrix10% %matrix6% %matrix8% %matrix2% %matrix7% %matrix4% 
set /a mat=1

goto :rand
:coucou
@ping localhost -n 3 >nul
echo #							
echo ############################
echo ### PREPARATION TERMINEE ###
echo ############################
echo #							
@ping localhost -n 3 >nul
goto :eof