import os

def updateDir(path):
    print "Updating: {0}".format(path)
    print "================"
    os.system("cd {0} && git pull".format(path))
    print "================\n\n"

def main():
    for path in os.listdir("./"):
        if os.path.isdir(path):
            updateDir(path)

if __name__ == '__main__':
    main()