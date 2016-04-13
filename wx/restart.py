import os

print("killing makeServer.py")
os.system("ps -ef | grep makeServer.py | grep -v grep | cut -c 9-15 | xargs kill -s 9")

print("restarting makeServer.py")
os.system("nohup python makeServer.py&")
