import os

title = '"Send from blat tool"'
body = '"xxxxxxxxx"'
address = "xxxxxxxxx@xxxx.com"
username = "xxxxxxxxx@163.com"
password = "xxxxxxxxx"
times = 1

os.system("blat -install smtp.163.com xxxxxxxxx@163.com 3 25")
for i in range(times):
    # os.system("blat -body " + body + " -to " + address + " -s "+ title +" -u " + username + " -pw "+ password)
    os.system\
        (
            "blat -body {} -to {} -s {} -u {} -pw {}".format\
                (
                    body,
                    address,
                    title,
                    username,
                    password,
                )
        )