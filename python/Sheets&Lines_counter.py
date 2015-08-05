#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, xlrd

fExt = ["XLS", "XLSX"]
reviewerAttendTimes = {}
creatorAttendTimes  = {}

targetFolder = ur"D:\KMWinDrv_VSS\011.IT5Color_v2.2\20150720-0723_FVT-1 Re\02.Coding_[PG作成]_PR_PM\code_review\Common"

def IsTargetFile(FileName):
    sufix = os.path.splitext(FileName)[1][1:]
    
    if sufix.upper() in fExt:
        return True

    else:
        return False

def countSheets(targetFile):
    print("Openning: " + targetFile.split("\\")[-1].encode("cp932"))
    xlsfile = xlrd.open_workbook(targetFile)

    try:
        lines = int(xlsfile.sheets()[0].cell(44 - 1, 38 - 1).value)
        participator = xlsfile.sheets()[0].cell(44 - 1, 17 - 1).value
    except:
        lines = 0
        participator = ""

    for p in participator.split("/")[0]:
        creatorAttendTimes[p] = creatorAttendTimes.get(p, 0) + 1
    for p in participator.split("/")[1:]:
        reviewerAttendTimes[p] = reviewerAttendTimes.get(p, 0) + 1

    table = True
    idx = 0
    while (table):
        try:
            table = xlsfile.sheets()[idx]
        except:
            break
        idx += 1

    # print participator.encode("cp932")
    print("Contains " + str(idx - 1) + " sheets")
    print("Contains " + str(lines) + " lines\n")
    return idx - 1, lines

def everyFile(targetFolder):
    sheets = []
    lines  = []
    FTuple = os.walk(targetFolder)
    for root, dirs, files in FTuple:
        for Tmpfile in files:
            if IsTargetFile(Tmpfile):
                of = os.path.join(root, Tmpfile)
                ret = countSheets(of)
                sheets.append(ret[0])
                lines.append(ret[1])

    return sheets, lines

if __name__ == '__main__':
    ret = everyFile(targetFolder)
    print("")
    print("Creator:")
    for p, t in creatorAttendTimes.items():
        print p.encode("cp932"), t
    print("Reviewer:")
    for p, t in reviewerAttendTimes.items():
        print p.encode("cp932"), t
    print("※TXTのCreatorとReviewerを統計しないのでご注意下さい\n")
    print("All: " + str(sum(ret[0])) + " sheets")
    print("All: " + str(sum(ret[1]) / 1000.0) + "k lines\n")


