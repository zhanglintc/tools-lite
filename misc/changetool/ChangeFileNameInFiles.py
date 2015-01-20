import os
import shutil
import re
import fileinput
import TxtFileHandle

"""
known bugs:
1. some change won't occure until you do it twice


"""

OrgFileName = """
thi_is_a_string_that_make_sure_no_content_can_match
""".split(",")

for i in range(len(OrgFileName)):
    OrgFileName[i] = OrgFileName[i].strip()
    
NewFileName = """
whatever_strings_here
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

	# ingore files
    file_name = fPathName.split('\\')[-1].lower()
    if file_name == "localize.ini" or file_name == "cst.ini":
        return

    TxtFile = TxtFileHandle.TxtFileHandle()
    generator = TxtFile.ReadTxtFile(fPathName)

    if generator == "":
        print("Error Read file:{}".format(fPathName))
        return
    
    to_be_wirtten = ""
    IsReplace = False
    for line in generator:
        idx = 0
        # No.1 replace by key word
        for keyword in OrgFileName:
            keywordstrip  = keyword.strip()

            if line.find(keywordstrip) != -1:
                line = line.replace(keywordstrip, NewFileName[idx])
                IsReplace = True
            idx = idx + 1

        # No.2 KOAY**_*.***  ->  KOAY**A*.*** 
        if re.search('(KOAY..).(.)', line): # old pattern: (KOAYC.).(.)
            line = re.sub('(KOAY..).(.)', lambda mc: mc.group(1) + 'A' + mc.group(2), line)
            IsReplace = True

        # No.3 deal with KONICA MINOLTA
        # need to be optimized
        if line.find("KONICA MINOLTA") != -1 and "INC" not in line:
            line = line.replace("KONICA MINOLTA", "Generic")
            IsReplace = True

        # No.4 KOPROFDL -> GNPROFDL
        if line.find("KOPROFDL") != -1:
            line = line.replace("KOPROFDL", "GNPROFDL")
            IsReplace = True

        # inf & unf !!!
        # inf [OEM URLS] %KM%="http://konicaminolta.jp/"
        # ppd

        # deal with c368
        if line.find("C368") != -1:
            line = line.replace("C368", "36C-9")
            IsReplace = True

        # deal with [OEM URLS]
        if "JA" in fPathName:
            if "[OEM URLS]" in line:
                line = ""

            if "http://konicaminolta.jp/" in line:
                line = ""

        to_be_wirtten += line

    # do replace
    if IsReplace:
        TxtFile.WriteTxtFile(to_be_wirtten)
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
        if re.search('(KOAY..).(.)', Tmpfile):
            replaced_file = re.sub('(KOAY..).(.)', lambda mc: mc.group(1) + 'A' + mc.group(2), Tmpfile)
            old_file = os.path.join(root, Tmpfile)
            new_file = os.path.join(root, replaced_file)
            os.rename(old_file, new_file)

