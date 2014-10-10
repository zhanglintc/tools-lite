import os
import shutil
import re
import fileinput
import TxtFileHandle

OrgFileName = """
old
""".split(",")

for i in range(len(OrgFileName)):
    OrgFileName[i] = OrgFileName[i].strip()
    
NewFileName = """
new
""".split(",")

for i in range(len(NewFileName)):
    NewFileName[i] = NewFileName[i].strip()
    
fExt = ["INI","SUB","PPD","INF","UNF","GPD","KMP"]
for i in range(len(fExt)):
    fExt[i] = fExt[i].strip().upper()
    
def IsTargetFile(FileName):
    sufix = os.path.splitext(FileName)[1][1:]
    
    if sufix.upper() in fExt:
        return True

    else:
        return False

def ProcessFile(fPathName):
    TxtFile = TxtFileHandle.TxtFileHandle()
    fStr = TxtFile.ReadTxtFile(fPathName)

    if fStr == "":
        print("Error Read file:{}".format(fPathName))
        return
    
    idx = 0
    IsReplace = False
    for keyword in OrgFileName:
        keywordstrip  = keyword.strip()

        if fStr.find(keywordstrip) != -1:
            fStr = fStr.replace(keywordstrip, NewFileName[idx])
            IsReplace = True
        idx = idx+1

    if IsReplace:
        TxtFile.WriteTxtFile( fStr )
        print("replced file: {}".format(fPathName) )
    
FTuple = os.walk(r"D:\ZDsoft_SVN\Zeus-S\PKI")
for root,dirs,files in FTuple:
    for Tmpfile in files:
        if IsTargetFile(Tmpfile):
            of = os.path.join(root,Tmpfile)
            #print("process:{}".format(of))
            ProcessFile(of)

