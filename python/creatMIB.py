#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="ZhangLin"

import os

targetFolder = r"E:\Subv_Work\IT5_Color_v3.0\KMSrc_2.06.31\Driver\Model"

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

tup = os.walk(targetFolder)
for root,dirs,files in tup:
    for f in files:
        if f.lower() == "basic.ini":
            fullPath = os.path.join(root, f)
            process(fullPath)

print("DeviceInfoCache Enable => Disable")

