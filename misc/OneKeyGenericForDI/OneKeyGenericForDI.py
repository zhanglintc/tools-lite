import os, sys
import shutil
import re
import fileinput
import TxtFileHandle

"""
Description:
  for DI folder special process.
"""

_title_   = "OneKeyGenericForDI"
_author_  = "ZhangLin"
_version_ = "v1.0"

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
"""

################################
# Need to be update -S
################################
fExt = ["INI", "SUB", "PPD", "INF", "UNF", "GPD", "KMP", "BAT"]
langList = ["DE", "EN", "ES", "FR", "IT", "JA", "KO", "ZH-CN", "ZH-TW"]

target_folder = ur"E:\Subv_Work\DI_9.2.0.0\IT5_Color_v3.0\KMSrc_2.06.34_5.0.5.0"

# folder name
oldFolder = "C658"
newFolder = "65C-9"

# model name
OwnName = """
C658,
C558,
C458,
C368,
C308,
C258,
C287,
C227,
""".split(",")

GenName = """
65C-9,
55C-9,
45C-9,
36C-9,
30C-9,
25C-9,
28C-8,
22C-8,
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

OwnProductID = """
0x233d,
0x231f,
0x2323,
""".split(",")

GenproductID = """
0x233e,
0x2320,
0x2324,
""".split(",")

if len(OwnName) != len(GenName) or len(oldINFStr) != len(newINFStr):
    sys.exit("Error: Quantity of strings not match(OwnName, GenName, oldINFStr, newINFStr)")

for i in range(len(OwnProductID)):
    if "0x" in OwnProductID[i]:
        OwnProductID[i] = OwnProductID[i].replace("0x", "")

for i in range(len(GenproductID)):
    if "0x" in GenproductID[i]:
        GenproductID[i] = GenproductID[i].replace("0x", "")

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
    if not generator:
        print("Error Read file:{}".format(fPathName))
        return

    IsReplace   = False
    jumpOneLine = False
    to_be_written = ""
    StartMenu = False
    PrgMang = False

    for line in generator:
        # No.1 deal with Lang.ini
        if "lang.ini" in file_name:
            # delete KONICA MINOLTA
            if ("KONICA MINOLTA " in line or " KONICA MINOLTA" in line) and StartMenu == False:
                line = line.replace("KONICA MINOLTA ", "")
                line = line.replace(" KONICA MINOLTA", "")
                IsReplace = True

            # delete Publisher=KONICA MINOLTA
            if "Publisher=KONICA MINOLTA" in line:
                line = line.replace("Publisher=KONICA MINOLTA\r\n", "")
                line = line.replace("Publisher=KONICA MINOLTA\r", "")
                line = line.replace("Publisher=KONICA MINOLTA\n", "")
                IsReplace = True

            # special process after [StartMenu] [PrgMang]
            if "[StartMenu]" in line:
                StartMenu = True

            if "[PrgMang]" in line:
                PrgMang = True

            if StartMenu == True:
                for i in range(len(OwnName)):
                    if line.find(OwnName[i].strip()) != -1 and ("Series" in line or "Mono" in line) and OwnName[i].strip():
                        line = line.replace(OwnName[i].strip(), GenName[i].strip())
                        IsReplace = True

                if "KONICA MINOLTA" in line and PrgMang == False:
                    line = line.replace("KONICA MINOLTA", "MFP-Printer Utility")
                    IsReplace = True

                if "KONICA MINOLTA" in line and PrgMang == True:
                    line = line.replace("KONICA MINOLTA", "Generic")
                    IsReplace = True

        # No.2 deal with Setup.ini
        if "setup.ini" in file_name:
            # deal with C658
            for i in range(len(OwnName)):
                if line.find(OwnName[i].strip()) != -1 and ("Series" in line or "Mono" in line) and OwnName[i].strip():
                    line = line.replace(OwnName[i].strip(), GenName[i].strip())
                    IsReplace = True

            # deal with UseSysDesc=0
            if "UseSysDesc=0" in line:
                line = line.replace("UseSysDesc=0", "UseSysDesc=1")
                IsReplace = True

            # deal with KONICA MINOLTA
            if "KONICA MINOLTA" in line:
                line = line.replace("KONICA MINOLTA", "MFP-Printer Utility")
                IsReplace = True

        # No.3 deal with Driver1.ini
        if re.search("driver.*", file_name):
            # deal with KONICA_MINOLTAC658SeEFA0
            for i in range(len(oldINFStr)):
                if line.find(oldINFStr[i].strip()) != -1 and oldINFStr[i].strip():
                    line = line.replace(oldINFStr[i].strip(), newINFStr[i].strip())
                    IsReplace = True

            # deal with C658
            for i in range(len(OwnName)):
                if line.find(OwnName[i].strip()) != -1 and OwnName[i].strip():
                    line = line.replace(OwnName[i].strip(), GenName[i].strip())
                    IsReplace = True

            # deal with ProductID
            for i in range(len(OwnProductID)):
                if line.find(OwnProductID[i].strip()) != -1 and OwnProductID[i].strip():
                    line = line.replace(OwnProductID[i].strip(), GenproductID[i].strip())
                    IsReplace = True

            # deal with KONICA MINOLTA
            if line.find("KONICA MINOLTA") != -1 and "INC" not in line:
                line = line.replace("KONICA MINOLTA", "Generic")
                IsReplace = True

            # KOAY**_*.***  ->  KOAY**A*.***
            if re.search('(KOAY..)[^A](.)', line) and not re.search('KOAY._COPY', line) and not re.search('KOAY._DATA', line):
                line = re.sub('(KOAY..)[^A](.)', lambda mc: mc.group(1) + 'A' + mc.group(2), line)
                IsReplace = True

            # deal with SearchSNMPID
            reg = '(\d.\d.\d.\d.\d.\d.\d\d\d\d\d.\d.)1(.\d.\d.\d.\d\d\d.\d.\d)'
            if re.search(reg, line):
                line = re.sub(reg, lambda mc: mc.group(1) + '2' + mc.group(2), line)
                IsReplace = True

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


