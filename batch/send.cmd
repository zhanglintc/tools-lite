blat -install smtp.163.com zhanglintc@163.com 3 25

set /a cnt=1

:loop
blat -body "%cnt%/1000条消息" -to zhanglintc@163.com -s "50条信息" -u zhanglintc@163.com -pw YOURPASSWORD

set /a cnt=%cnt%+1
if %cnt% lss 50 goto loop
pause