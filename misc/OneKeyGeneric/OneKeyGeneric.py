import os
import shutil
import re
import fileinput
import TxtFileHandle

"""
Nothing here...
"""
################################
# Need to be update -S
################################
fExt = ["INI", "SUB", "PPD", "INF", "UNF", "GPD", "KMP", "BAT"]
langList = ["DE", "EN", "ES", "FR", "IT", "JA", "KO", "ZH-CN", "ZH-TW"]

target_folder = r"E:\ZDS_Working_SVN\trunk\KMSrc_2.06.10\Driver\Model\C368"

# model name
OwnName = "C368"
GenName = "36C-9"

# this string is in *.INF
oldINFStr = "KONICA_MINOLTAC368Se6AA6"
newINFStr = "Generic36C-9SeriesB942"

################################
# Need to be update -E
################################

OrgFileName = """
thi_is_a_string_that_no_content_can_match,
""".split(",")
for i in range(len(OrgFileName)):
    OrgFileName[i] = OrgFileName[i].strip()    
NewFileName = """
whatever_strings_here,
""".split(",")
for i in range(len(NewFileName)):
    NewFileName[i] = NewFileName[i].strip()
for i in range(len(fExt)):
    fExt[i] = fExt[i].strip().upper()

################################################################
def IsTargetFile(FileName):
    sufix = os.path.splitext(FileName)[1][1:]
    
    if sufix.upper() in fExt:
        return True

    else:
        return False
################################################################

################################################################
def ProcessFile(fPathName):
    """
    Replace content in files.
    """
################################
	# ingore files
    file_name = fPathName.split('\\')[-1].lower()
    if "localize" in file_name or file_name == "cst.ini":
        return
################################
    # get language folder
    langFolder = fPathName.split("\\")[-2].upper()
################################
    TxtFile = TxtFileHandle.TxtFileHandle()
    generator = TxtFile.ReadTxtFile(fPathName)

    if generator == "":
        print("Error Read file:{}".format(fPathName))
        return
################################
    to_be_written = ""
    IsReplace = False
    jumpOneLine = False
    for line in generator:
        idx = 0
################################################################
        # No.0 replace by key word
        for keyword in OrgFileName:
            keywordstrip  = keyword.strip()

            if line.find(keywordstrip) != -1:
                line = line.replace(keywordstrip, NewFileName[idx])
                IsReplace = True
            idx = idx + 1
################################################################
        # No.1 deal with *INF String
        if line.find(oldINFStr) != -1:
            line = line.replace(oldINFStr, newINFStr)
            IsReplace = True
################################################################
        # No.2 KOAY**_*.***  ->  KOAY**A*.*** 
        if re.search('(KOAY..)[^A](.)', line): # old pattern: (KOAYC.).(.)
            line = re.sub('(KOAY..)[^A](.)', lambda mc: mc.group(1) + 'A' + mc.group(2), line)
            IsReplace = True
################################################################
        # No.3 deal with KONICA MINOLTA
        if line.find("KONICA MINOLTA") != -1 and "INC" not in line:
            line = line.replace("KONICA MINOLTA", "Generic")
            IsReplace = True
################################################################
        # No.4 KOPROFDL -> GNPROFDL
        if line.find("KOPROFDL") != -1:
            line = line.replace("KOPROFDL", "GNPROFDL")
            IsReplace = True
################################################################
        # No.5 deal with C368
        if line.find(OwnName) != -1:
            line = line.replace(OwnName, GenName)
            IsReplace = True
################################################################
        # No.6 deal with [OEM URLS]
        if "JA" in fPathName or langFolder not in langList:
            if jumpOneLine == True:
                line = ""
                jumpOneLine = False

            if "[OEM URLS]" in line:
                line = ""

            if "http://konicaminolta.jp/" in line:
                line = ""
                jumpOneLine = True

            if "http://konicaminolta.com/" in line:
                line = ""
                jumpOneLine = True
################################################################
        # append this line to the end
        to_be_written += line
################################################################
    # do replace
    if IsReplace:
        TxtFile.WriteTxtFile(to_be_written)
        print("replced file: {}".format(fPathName))
################################################################
FTuple = os.walk(target_folder)
for root,dirs,files in FTuple:
    for Tmpfile in files:
        # replace file content
        if IsTargetFile(Tmpfile):
            of = os.path.join(root,Tmpfile)
            ProcessFile(of)
################################################################
        # replace file name
        if re.search('(KOAY..)[^A](.)', Tmpfile):
            replaced_file = re.sub('(KOAY..)[^A](.)', lambda mc: mc.group(1) + 'A' + mc.group(2), Tmpfile)
            old_file = os.path.join(root, Tmpfile)
            new_file = os.path.join(root, replaced_file)
            os.rename(old_file, new_file)
################################################################


