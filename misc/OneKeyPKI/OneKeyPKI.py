#!/usr/bin/env python
# -*- coding: utf-8 -*-

import TxtFileHandle
import os, re

fExt = ["INI", "SUB", "PPD", "INF", "UNF", "GPD", "KMP", "BAT", "DEF"]

theComment = u"2015.08.06 ZhangLin PKI対応テスト"
targetFolder = r"C:\Users\Lane\Desktop\958"


def processFile(targetFile):
    fExt  = targetFile.split(".")[-1]
    fName = targetFile.split("\\")[-1]
    """
    1. userenv.bat => userenv_PKI.bat

    修正後:    userenv.bat を削除し、userenv_PKI.bat を用意する

    修正後:    set RASTER_PKI=FALSE
    修正後:    :set RASTER_PKI=TRUE

    修正前:    set RASTER_PKI_SSO=FALSE
    修正前:    :set RASTER_PKI_SSO=TRUE
            ↓
    修正後:    :set RASTER_PKI_SSO=FALSE
    修正後:    set RASTER_PKI_SSO=TRUE
    """
    pass


    """
    2. CUSTOM\(機種名)\DLGTYPE\dlgtype.def

    修正前:    PKI_Mode_Build =            0
            ↓
    修正後:    PKI_Mode_Build =            2
    """
    if fExt.lower() == "def":
        TxtFile = TxtFileHandle.TxtFileHandle()
        generator = TxtFile.ReadTxtFile(targetFile)

        toBeWritten = ""
        doReplace = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("PKI_Mode_Build.*0", line) and "#" not in line:
                toBeWritten += "#// " + theComment + " -S\r\n"
                toBeWritten += "#// " + line
                toBeWritten += line.replace("0", "2")
                toBeWritten += "#// " + theComment + " -E\r\n"
                doReplace = True
                continue

            toBeWritten += line

        if doReplace:
            TxtFile.WriteTxtFile(toBeWritten)
            print("replced file: {}".format(targetFile))

    """
    3. Basic.ini (PCL/PS共通)

    [Version]                                   
    修正前:    Ver_Basic=          *00             ※"*"の値は任意
            ↓
    修正後:    Ver_Basic=          *10

    [FeatureSetting]
    修正前:    AuthenticationVerify=           Enable
            ↓
    修正後:    ;// AuthenticationVerify=           Enable
    修正後:    AuthenticationVerify=           Disable
    修正後:    ICCardUsed=                     Enable

    修正前:    VerifyAuthentic=            Enable
            ↓
    修正後:    ;// VerifyAuthentic=            Enable
    修正後:    VerifyAuthentic=            Disable
    修正後:    PopupAuthentic=             Disable

    [EasySetPreset]
    修正前:    ES_005=KOAYC*_E.KMP
    修正前:    ES_006=KOAYC*_F.KMP
    修正前:    ES_007=KOAYC*_G.KMP
            ↓
    修正後:    ;// ES_005=KOAYC*_E.KMP                         ※MonoのKMPは不要なので、コメント化
    修正後:    ;// ES_006=KOAYC*_F.KMP
    修正後:    ;// ES_007=KOAYC*_G.KMP
    """
    if fName.lower() == "basic.ini":
        TxtFile = TxtFileHandle.TxtFileHandle()
        generator = TxtFile.ReadTxtFile(targetFile)

        toBeWritten = ""
        doReplace = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("Ver_Basic.*\d(0)0", line):
                doReplace = True
                line = re.sub("(Ver_Basic.*?\d)0(0)", lambda mc: mc.group(1) + '1' + mc.group(2), line)

            if re.search("AuthenticationVerify.*Enable", line) and ";//" not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                toBeWritten += "AuthenticationVerify=           Disable\r\n"
                toBeWritten += "ICCardUsed=                     Enable\r\n"
                toBeWritten += ";// " + theComment + " -E\r\n"
                doReplace = True
                continue

            if re.search("VerifyAuthentic.*Enable", line) and ";//" not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                toBeWritten += "VerifyAuthentic=            Disable\r\n"
                toBeWritten += "PopupAuthentic=             Disable\r\n"
                toBeWritten += ";// " + theComment + " -E\r\n"
                doReplace = True
                continue

            # [EasySetPreset], not completed
            pass

            toBeWritten += line

        if doReplace:
            TxtFile.WriteTxtFile(toBeWritten)
            print("replced file: {}".format(targetFile))

    """
    4. Command.ini (PCL/PS共通)

    [Version]
    修正前:    Ver_Command=            *00             ※"*"の値は任意
            ↓                                   
    修正後:    Ver_Command=            *10

    [PJL_StartCommand]
    修正前:    Order=          NonUI1, …, NonUI2                ※PJLコマンドはNonUI1から始まり、
                                                                NonUI2で終わるように構成されている
            ↓
    修正後:    Order=          Pki, SingleSignOn, NonUI1, …, NonUI2            ※PkiとSingleSignOnのコマンドを先に投げることで
                                                                                特殊な処理に入る
    修正後:                                　（先頭以外に追加しても機能しないので注意）
    修正前:     SubSection=            NonUI1, …, SingleSignOn
                                        2015/1/15侯リ園補足
            ↓                                   
    修正後:     SubSection=            Pki, NonUI1, …, SingleSignOn

    追加: ; ---------------------------                           ※以下、[PJL_StartCommand]と[NonUI1]の間に追加
    追加: ; for PKI 
    追加: ; ---------------------------
    追加: [Pki]
    追加: PkiStartJob=            "\x1B%-12345X@PJL JOB\r\n"
    追加: PkiCoe=                 "@PJL SET KMPKICOE = %s{API(PkiCoe),321,UTF8,None}\r\n"                     この行を使用する（2014.10.21から）
    追加: PkiUserName=            "@PJL SET KMPKIUSERNAME = \"%s{API(PkiUserName),64,UTF8,None}\"\r\n"
    追加: PkiCertServType=        "@PJL SET KMPKICERTSERVTYPE = %s{API(PkiCertServType),64,UTF8,None}\r\n"
    追加: PkiCertServNum=         "@PJL SET KMPKICERTSERVNUM = %s{UI(PkiCertServNum),4,,None}\r\n"

    追加: PkiComment=             "@PJL COMMENT = \"PKIPrintData\"\r\n"               ※[NonUI1]の"Comment="と"UserName="の間に追加
    """
    if fName.lower() == "command.ini":
        TxtFile = TxtFileHandle.TxtFileHandle()
        generator = TxtFile.ReadTxtFile(targetFile)

        toBeWritten = ""
        doReplace = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("Ver_Command.*\d(0)0", line):
                doReplace = True
                line = re.sub("(Ver_Command.*?\d)0(0)", lambda mc: mc.group(1) + '1' + mc.group(2), line)

            if re.search("Order.*NonUI1.*SingleSignOn,NonUI2", line) and ";//" not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                line = line.replace(",SingleSignOn", "")
                line = line.replace("NonUI1", "Pki,SingleSignOn,NonUI1")
                toBeWritten += line
                toBeWritten += ";// " + theComment + " -E\r\n"
                doReplace = True
                continue

            if re.search("SubSection.*NonUI1.*SingleSignOn", line) and ";//" not in line and "Pki," not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                line = line.replace("NonUI1", "Pki,NonUI1")
                toBeWritten += line
                toBeWritten += ";// " + theComment + " -E\r\n"
                doReplace = True
                continue

            toBeWritten += line

        if doReplace:
            TxtFile.WriteTxtFile(toBeWritten)
            print("replced file: {}".format(targetFile))

def isTargetFile(FileName):
    sufix = os.path.splitext(FileName)[1][1:]
    
    if sufix.upper() in fExt:
        return True

    else:
        return False

if __name__ == '__main__':
    tup = os.walk(targetFolder)
    for root, dirs, files in tup:
        for f in files:
            if isTargetFile(f):
                targetFile = os.path.join(root, f)
                processFile(targetFile)