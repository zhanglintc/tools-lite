# -*- coding: utf-8 -*-

import os, sys
import re

fExt = ["KMP"]

for i in range(len(fExt)):
    fExt[i] = fExt[i].strip().upper()
    
def IsTargetFile(FileName):
    sufix = os.path.splitext(FileName)[1][1:]
    
    if sufix.upper() in fExt:
        return True
    else:
        return False

def ProcessFile(fPathName, OENver, GENver, PKIver):
    fr = open(fPathName, "rb")
    fStr = fr.read()
    fr.close()

    if fStr == "":
        print("Error Read file:{}".format(fPathName))
        return
    
    isReplace = False
    mc = re.search('version=\"(.*?)\"', fStr)
    if mc:
        # PKI process
        if "PKI" in fPathName:
            fStr = fStr.replace('version="{0}"'.format(mc.group(1)), 'version="{0}"'.format(PKIver))

        # GEN process
        elif "-" in fPathName:
            fStr = fStr.replace('version="{0}"'.format(mc.group(1)), 'version="{0}"'.format(GENver))

        # OWN process
        else:
            fStr = fStr.replace('version="{0}"'.format(mc.group(1)), 'version="{0}"'.format(OENver))

        isReplace = True

    if isReplace:
        fw = open(fPathName, "wb")
        fw.write(fStr)
        fw.close()
        print("replced file: {}".format(fPathName) )
        return True

    else:
        return False

def main():
    if  len(sys.argv) != 5:
        print('KMPVerUP [Version 1.0] => A tool makes KMP file version up.')
        print('Powered by ZhangLin. Nothing reserved.')
        print('')
        print('')
        print('Usage:')
        print('  KMPVerUp folder1|folder2|folderN OENver GENver PKIver')
        print('')
        print('Note:')
        print('  This is not the main entry file,')
        print('  please call this file by using "VersionUp_Tool.xlsm".')
        print('')
        print(u'ノート:'.encode("cp932"))
        print(u'  このファイルはアプリ本体ではない,'.encode("cp932"))
        print(u'  "VersionUp_Tool.xlsm"を利用ください.'.encode("cp932"))

        try:
            input()
        except:
            pass

        return -1

    targetFolderStr = sys.argv[1]   # **/Model/C658|**/Model/C658FA => split by "|"
    OENver = sys.argv[2]            # eg: 5.0.13.0 => no quotation
    GENver = sys.argv[3]            # eg: 5.0.13.0 => no quotation
    PKIver = sys.argv[4]            # eg: 5.0.13.OSW1_01 => no quotation

    targetFoderList = targetFolderStr.split("|")
    KMPCount = 0
    for targetFolder in targetFoderList:
        FTuple = os.walk(targetFolder)
        for root, dirs, files in FTuple:
            for Tmpfile in files:
                if IsTargetFile(Tmpfile):
                    of = os.path.join(root, Tmpfile)
                    if ProcessFile(of, OENver, GENver, PKIver):
                        KMPCount += 1

    return KMPCount


if __name__ == '__main__':
    exitCode = main()
    sys.exit(exitCode)


