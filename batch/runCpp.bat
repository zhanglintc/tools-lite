@ECHO OFF 
cd %~dp1 

ECHO Compiling %~nx1 ....... 
g++ %~nx1 
echo=
ECHO -----------OUTPUT----------- 
start %~n1 
