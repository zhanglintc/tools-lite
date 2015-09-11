import os, sys
import shutil
import re
import fileinput
import TxtFileHandle

_author_  = "ZhangLin"
_version_ = "v1.1"

"""
                   _ooOoo_ 
                  o8888888o 
                  88" . "88 
                  (| -_- |) 
                  O\  =  /O 
               ____/`---'\____ 
             .'  \\|     |//  `. 
            /  \\|||  :  |||//  \ 
           /  _||||| -:- |||||-  \ 
           |   | \\\  -  /// |   | 
           | \_|  ''\---/''  |   | 
           \  .-\__  `-`  ___/-. / 
         ___`. .'  /--.--\  `. . __ 
      ."" '<  `.___\_<|>_/___.'  >'"". 
     | | :  `- \`.;`\ _ /`;.`/ - ` : | | 
     \  \ `-.   \_ __\ /__ _/   .-` /  / 
======`-.____`-.___\_____/___.-`____.-'====== 
                   `=---=' 

Todo:
1. add some comment
2. ignore DriverName in *.ini
"""

################################
# Need to be update -S
################################
fExt = ["INI", "SUB", "PPD", "INF", "UNF", "GPD", "KMP", "BAT"]
langList = ["DE", "EN", "ES", "FR", "IT", "JA", "KO", "ZH-CN", "ZH-TW"]

target_folder = ur"E:\Subv_Work\IT5_Color_v3.0\KMSrc_2.06.34\Driver\Model"

# folder name
oldFolder = "C658"
newFolder = "65C-9"

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
            if line.find(oldINFStr[i].strip()) != -1 and oldINFStr[i].strip():
                line = line.replace(oldINFStr[i].strip(), newINFStr[i].strip())
                IsReplace = True

        # No.2 KOAY**_*.***  ->  KOAY**A*.***  @but not change _COPY or _DATA
        if re.search('(KOAY..)[^A](.)', line) and not re.search('KOAY._COPY', line) and not re.search('KOAY._DATA', line):
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
            if line.find(OwnName[i].strip()) != -1 and ("Series" in line or "Mono" in line) and OwnName[i].strip():
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
        print("replace file: {}".format(fPathName))

if __name__ == '__main__':
    # No.1 replace file content
    print("Replace file content:")
    FTuple = os.walk(target_folder)
    for root, dirs, files in FTuple:
        if "PKI" in root:
            continue

        for Tmpfile in files:
            if IsTargetFile(Tmpfile):
                of = os.path.join(root, Tmpfile)
                ProcessFile(of)

    print("End of file content")

    # No.2 replace file name
    print("")
    print("Replace file name:")
    FTuple = os.walk(target_folder)
    for root, dirs, files in FTuple:
        if "PKI" in root:
            continue

        for Tmpfile in files:
            if re.search('(KOAY..)[^A](.)', Tmpfile):
                replaced_file = re.sub('(KOAY..)[^A](.)', lambda mc: mc.group(1) + 'A' + mc.group(2), Tmpfile)
                old_file = os.path.join(root, Tmpfile)
                new_file = os.path.join(root, replaced_file)
                os.rename(old_file, new_file)
                print("change name: {0} => {1}".format(old_file.split("\\")[-1], new_file.split("\\")[-1]))

    print("End of file name")

    # No.3 replace folder name
    print("")
    print("change folder name:")
    rootContainer = []
    FTuple = os.walk(target_folder)
    for root, dirs, files in FTuple:
        rootContainer.append(root)

    for i in range(len(rootContainer) - 1, -1, -1):
        root = rootContainer[i]

        if "PKI" in root:
            continue

        if os.path.isdir(root):
            s = os.path.split(root)

            # Printer folder
            if s[1] == oldFolder:
                try:
                    os.rename(root, s[0]+ "\\" + newFolder)
                    print("{0} ---> {1}".format(root, newFolder))
                except:
                    print("Error: {0} ---> {1} failed".format(os.path.join(root, oldFolder), newFolder))

            # FAX folder
            if s[1] == oldFolder + "FA":
                try:
                    os.rename(root, s[0]+ "\\" + newFolder + "FA")
                    print("{0} ---> {1}".format(root, newFolder + "FA"))
                except:
                    print("Error: {0} ---> {1} failed".format(os.path.join(root, oldFolder + "FA"), newFolder + "FA"))

    print("End of folder name")


