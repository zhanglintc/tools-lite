import os

title = '"在哪儿，来不来？"'
body = '"你回家了？"'
address = "0801jcjhz@163.com"
username = "zhanglintc@163.com"
password = "l0velin7211"
times = 1

os.system("blat -install smtp.163.com zhanglintc@163.com 3 25")
for i in range(times):
    os.system("blat -body " + body + " -to " + address + " -s "+title +" -u " + username + " -pw "+ password)