import os, sys
import shutil
import re
import fileinput
import TxtFileHandle

"""
Nothing here...
"""

_author_  = "ZhangLin"
_version_ = "1.1"

################################
# Need to be update -S
################################
fExt = ["INI", "SUB", "PPD", "INF", "UNF", "GPD", "KMP", "BAT"]
langList = ["DE", "EN", "ES", "FR", "IT", "JA", "KO", "ZH-CN", "ZH-TW"]

target_folder = ur"E:\Subv_Work\IT5_Color_v3.0\KMSrc_2.06.34\Driver\Model\C658\CUSTOM\INSTALL\PCLXL\Win2kXP\JA"

# model name
OwnName = """
C658,
C368,
C287,
""".split(",")

GenName = """
65C-9,
36C-9,
28C-8,
""".split(",")


# this string is in *.INF
oldINFStr = """
KONICA_MINOLTAC658SeEFA0,
KONICA_MINOLTAC368Se6AA6,
KONICA_MINOLTAC287Se76D5,
""".split(",")

newINFStr = """
Generic65C-9Series7AA3,
Generic36C-9SeriesB942,
Generic28C-8Series7037,
""".split(",")

if len(OwnName) != len(GenName) or len(OwnName) != len(oldINFStr):
    sys.exit("Error: Quantity of strings not match(OwnName, GenName, oldINFStr, newINFStr)")

################################
# Need to be update -E
################################

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

    file_name  = fPathName.split('\\')[-1].lower()
    langFolder = fPathName.split("\\")[-2].upper()
    TxtFile    = TxtFileHandle.TxtFileHandle()
    generator  = TxtFile.ReadTxtFile(fPathName)

    # ignore localize and cst
    if "localize" in file_name or file_name == "cst.ini":
        return

    # fail to open file
    if generator == "":
        print("Error Read file:{}".format(fPathName))
        return

    IsReplace   = False
    jumpOneLine = False
    to_be_written = ""

    for line in generator:
        # No.1 deal with *INF String
        for i in range(len(oldINFStr)):
            if line.find(oldINFStr[i].strip()) != -1:
                line = line.replace(oldINFStr[i].strip(), newINFStr[i].strip())
                IsReplace = True

        # No.2 KOAY**_*.***  ->  KOAY**A*.*** 
        if re.search('(KOAY..)[^A](.)', line): # old pattern: (KOAYC.).(.)
            if re.search('KOAY._COPY', line) or re.search('KOAY._DATA', line): # jump KOAY8_COPY or KOAY8_DATA
                line = line
            else:
                line = re.sub('(KOAY..)[^A](.)', lambda mc: mc.group(1) + 'A' + mc.group(2), line)
            IsReplace = True

        # No.3 deal with KONICA MINOLTA
        if line.find("KONICA MINOLTA") != -1 and "INC" not in line:
            line = line.replace("KONICA MINOLTA", "Generic")
            IsReplace = True

        # No.4 KOPROFDL -> GNPROFDL
        if line.find("KOPROFDL") != -1:
            line = line.replace("KOPROFDL", "GNPROFDL")
            IsReplace = True

        # No.5 deal with C658
        for i in range(len(OwnName)):
            if line.find(OwnName[i].strip()) != -1:
                line = line.replace(OwnName[i].strip(), GenName[i].strip())
                IsReplace = True

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

        # append this line to the end
        to_be_written += line

    # do replace
    if IsReplace:
        TxtFile.WriteTxtFile(to_be_written)
        print("replced file: {}".format(fPathName))

if __name__ == '__main__':
    FTuple = os.walk(target_folder)
    for root,dirs,files in FTuple:
        for Tmpfile in files:
            # No.1: replace file content
            if IsTargetFile(Tmpfile):
                of = os.path.join(root,Tmpfile)
                ProcessFile(of)

            # No.2: replace file name
            if re.search('(KOAY..)[^A](.)', Tmpfile):
                replaced_file = re.sub('(KOAY..)[^A](.)', lambda mc: mc.group(1) + 'A' + mc.group(2), Tmpfile)
                old_file = os.path.join(root, Tmpfile)
                new_file = os.path.join(root, replaced_file)
                os.rename(old_file, new_file)



