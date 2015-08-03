#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="ZhangLin"

import os, sys

version = sys.version[0]

targetFolder = r""

def QuotationStrip(targetFolder):
    """
    Strip quotation mark of given path
    """

    if targetFolder[0] == '\"':
        targetFolder = targetFolder[1:-1]

    return targetFolder

def process(givenPath):
    toBeWriten = ""
    fr = open(givenPath, "rb")
    line = True
    while line:
        line = fr.readline()
        if "DeviceInfoCache" in line:
            line = line.replace("Enable", "Disable")
        toBeWriten += line
    fr.close()

    fw = open(givenPath, "wb")
    print("Writing: " + givenPath)
    fw.write(toBeWriten)
    fw.close()

if __name__ == '__main__':
    if not targetFolder:
        if version == '2':
            targetFolder = raw_input("Drag target folder here:\n")
        if version == '3':
            targetFolder = input("Drag target folder here:\n")

        if not targetFolder:
            print('"targetFolder" not set. Script is going to terminate.')

            try:
                input()
            except:
                pass

            sys.exit(0)

        targetFolder = QuotationStrip(targetFolder)

    tup = os.walk(targetFolder)
    for root,dirs,files in tup:
        for f in files:
            if f.lower() == "basic.ini":
                fullPath = os.path.join(root, f)
                process(fullPath)

    print("")
    print("DeviceInfoCache Enable => Disable")

    try:
        input()
    except:
        pass

