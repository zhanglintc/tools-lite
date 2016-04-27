import os, sys

print("killing fileServer.py")
os.system("ps -ef | grep fileServer.py | grep -v grep | cut -c 9-15 | xargs kill -s 9")

if len(sys.argv) == 2 and sys.argv[1] == "shut":
    sys.exit(0)

print("restarting fileServer.py")
os.system("sudo nohup python fileServer.py&")

