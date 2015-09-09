import os, sys
import shutil
import re
import fileinput
import TxtFileHandleDev

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

target_folder = ur"xxx"

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
    if not generator:
        print("Error Read file:{}".format(fPathName))
        return

    IsReplace   = False
    jumpOneLine = False
    to_be_written = ""

    for line in generator:
        # Lang.ini
        
        line = line.replace("KONICA MINOLTA ", "")
        line = line.replace(" KONICA MINOLTA", "")
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
        for Tmpfile in files:
            if IsTargetFile(Tmpfile):
                of = os.path.join(root, Tmpfile)
                ProcessFile(of)

    print("End of file content")


