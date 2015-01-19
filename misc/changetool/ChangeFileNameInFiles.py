import os
import shutil
import re
import fileinput
import TxtFileHandle

OrgFileName = """

""".split(",")

for i in range(len(OrgFileName)):
    OrgFileName[i] = OrgFileName[i].strip()
    
NewFileName = """

""".split(",")

for i in range(len(NewFileName)):
    NewFileName[i] = NewFileName[i].strip()
    
fExt = ["INI", "SUB", "PPD", "INF", "UNF", "GPD", "KMP"]
for i in range(len(fExt)):
    fExt[i] = fExt[i].strip().upper()
    
def IsTargetFile(FileName):
    sufix = os.path.splitext(FileName)[1][1:]
    
    if sufix.upper() in fExt:
        return True

    else:
        return False

def ProcessFile(fPathName):
    """
    Replace content in files.
    """

    TxtFile = TxtFileHandle.TxtFileHandle()
    fStr = TxtFile.ReadTxtFile(fPathName) # todo: try to meke ReadTxtFile return one line each time

    if fStr == "":
        print("Error Read file:{}".format(fPathName))
        return
    
    idx = 0
    IsReplace = False
    # No.1 replace by key word
    for keyword in OrgFileName:
        keywordstrip  = keyword.strip()

        if fStr.find(keywordstrip) != -1:
            fStr = fStr.replace(keywordstrip, NewFileName[idx])
            IsReplace = True
        idx = idx + 1

    # No.2 KOAYC*_*.***  ->  KOAYC*A*.*** 
    if re.search('(KOAYC.).(.)', fStr):
        fStr = re.sub('(KOAYC.).(.)', lambda mc: mc.group(1) + 'A' + mc.group(2), fStr)
        IsReplace = True

    # No.3 deal with KONICA MINOLTA
    # need to be optimized
    if fStr.find("KONICA MINOLTA") != -1:
        fStr = fStr.replace("KONICA MINOLTA", "Generic")
        IsReplace = True

    # No.4 KOPROFDL -> GNPROFDL
    if fStr.find("KOPROFDL") != -1:
        fStr = fStr.replace("KOPROFDL", "GNPROFDL")
        IsReplace = True

    # inf & unf !!!
    # inf [OEM URLS] %KM%="http://konicaminolta.jp/"
    # ppd

    # deal with c368
    if fStr.find("C368") != -1:
        fStr = fStr.replace("C368", "36C-9")
        IsReplace = True

    # do replace
    if IsReplace:
        TxtFile.WriteTxtFile(fStr)
        print("replced file: {}".format(fPathName))
    
FTuple = os.walk(r"E:\ZDS_Working_SVN\trunk\ZeusS_v2.1\KMSrc_2.06.10\Driver\Model\C368_3")
for root,dirs,files in FTuple:
    for Tmpfile in files:
        # replace file content
        if IsTargetFile(Tmpfile):
            of = os.path.join(root,Tmpfile)
            #print("process:{}".format(of))
            ProcessFile(of)

        # replace file name
        if re.search('(KOAYC.).(.)', Tmpfile):
            replaced_file = re.sub('(KOAYC.).(.)', lambda mc: mc.group(1) + 'A' + mc.group(2), Tmpfile)
            old_file = os.path.join(root, Tmpfile)
            new_file = os.path.join(root, replaced_file)
            os.rename(old_file, new_file)

