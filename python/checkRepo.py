#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

tempFile = "tempFile"

def updateDir(path):
    tempFilePath = "{0}/{1}".format(path, tempFile)

    # write log to a temp file
    os.system("cd {0} && git status > {1}".format(path, tempFile))

    # read it
    fr = open(tempFilePath, "rb")
    content = fr.read()
    fr.close()

    # notify if not up-to-date
    if "up-to-date" not in content:
        print path

    # remove temp file
    os.remove(tempFilePath)

def main():
    for path in os.listdir("./"):
        if os.path.isdir(path):
            updateDir(path)

if __name__ == '__main__':
    main()