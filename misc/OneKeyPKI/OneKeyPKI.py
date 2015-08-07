#!/usr/bin/env python
# -*- coding: utf-8 -*-

import TxtFileHandle
import os, re
import shutil

doReplace = False

fExt = ["INI", "SUB", "PPD", "INF", "UNF", "GPD", "KMP", "BAT", "DEF"]

theComment = u"2015.08.06 ZhangLin WBS No.55 PKI対応テスト"
targetFolder = r"E:\Subv_Work\IT5_Color_v3.0\KMSrc_2.06.31\Driver\Model\C658"


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
        isFind = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("PKI_Mode_Build.*0", line) and "#" not in line:
                toBeWritten += "#// " + theComment + " -S\r\n"
                toBeWritten += "#// " + line
                toBeWritten += line.replace("0", "2")
                toBeWritten += "#// " + theComment + " -E\r\n"
                isFind = True
                continue

            toBeWritten += line

        if doReplace and isFind:
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
        isFind = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("Ver_Basic.*\d(0)0", line):
                line = re.sub("(Ver_Basic.*?\d)0(0)", lambda mc: mc.group(1) + '1' + mc.group(2), line)
                isFind = True

            if re.search("AuthenticationVerify.*Enable", line) and ";//" not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                toBeWritten += "AuthenticationVerify=           Disable\r\n"
                toBeWritten += "ICCardUsed=                     Enable\r\n"
                toBeWritten += ";// " + theComment + " -E\r\n"
                isFind = True
                continue

            if re.search("VerifyAuthentic.*Enable", line) and ";//" not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                toBeWritten += "VerifyAuthentic=            Disable\r\n"
                toBeWritten += "PopupAuthentic=             Disable\r\n"
                toBeWritten += ";// " + theComment + " -E\r\n"
                isFind = True
                continue

            for n in ["05", "06", "07", "12", "13", "14", "19", "20", "21"]:
                if re.search("ES_0" + n, line) and ";//" not in line:
                    line = ";// " + line
                    isFind = True

            toBeWritten += line

        if doReplace and isFind:
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
        isFind = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("Ver_Command.*\d(0)0", line):
                line = re.sub("(Ver_Command.*?\d)0(0)", lambda mc: mc.group(1) + '1' + mc.group(2), line)
                isFind = True

            if re.search("Order.*NonUI1.*SingleSignOn,NonUI2", line) and ";//" not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                line = line.replace(",SingleSignOn", "")
                line = line.replace("NonUI1", "Pki,SingleSignOn,NonUI1")
                toBeWritten += line
                toBeWritten += ";// " + theComment + " -E\r\n"
                isFind = True
                continue

            if re.search("SubSection.*NonUI1.*SingleSignOn", line) and ";//" not in line and "Pki," not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                line = line.replace("NonUI1", "Pki,NonUI1")
                toBeWritten += line
                toBeWritten += ";// " + theComment + " -E\r\n"
                isFind = True
                continue

            if re.search("\[NonUI1\]", line) and ";//" not in line:
                toBeWritten += "    ;// " + theComment + " -S\r\n"
                toBeWritten += "    ; ---------------------------\r\n"
                toBeWritten += "    ; for PKI\r\n"
                toBeWritten += "    ; ---------------------------\r\n"
                toBeWritten += "    [Pki]\r\n"
                toBeWritten += '    PkiStartJob=            "\\x1B%-12345X@PJL JOB\\r\\n"' + "\r\n"
                toBeWritten += '    PkiCoe=                 "@PJL SET KMPKICOE = %s{API(PkiCoe),321,UTF8,None}\\r\\n"' + "\r\n"
                toBeWritten += '    PkiUserName=            "@PJL SET KMPKIUSERNAME = \\"%s{API(PkiUserName),64,UTF8,None}\\"\\r\\n"' + "\r\n"
                toBeWritten += '    PkiCertServType=        "@PJL SET KMPKICERTSERVTYPE = %s{API(PkiCertServType),64,UTF8,None}\\r\\n"' + "\r\n"
                toBeWritten += '    PkiCertServNum=         "@PJL SET KMPKICERTSERVNUM = %s{UI(PkiCertServNum),4,,None}\\r\\n"' + "\r\n"
                toBeWritten += "    ;// " + theComment + " -E\r\n\r\n"
                toBeWritten += line
                # isFind = True
                continue

            if re.search("Comment=", line) and ";//" not in line:
                toBeWritten += line
                toBeWritten += "    ;// " + theComment + " -S\r\n"
                toBeWritten += '    PkiComment=             "@PJL COMMENT = \\"PKIPrintData\\"\\r\\n"' + "\r\n"
                toBeWritten += "    ;// " + theComment + " -E\r\n"
                # isFind = True
                continue

            toBeWritten += line

        if doReplace and isFind:
            TxtFile.WriteTxtFile(toBeWritten)
            print("replced file: {}".format(targetFile))

    """
    6. UISetup.ini (PCL/PS共通)

    [Version]
    修正前:    Ver_UISetup=            *00             ※"*"の値は任意
            ↓
    修正後:    Ver_UISetup=            *10

    [DeviceOption] 
    修正前:    Order=          OpMachine, …, DevUserAuthentication, …, OpWLAN_ErpRet
            ↓
    修正後:    Order=          OpMachine, …, DevTPMStatus, …, OpWLAN_ErpRet                ※DevUserAuthenticationを削除し、DevTPMStatusを追加

    修正前:    LinkSection=            OpMachine, …,  …, OpWLAN_ErpRet
                                            2015/7/16 張麟補足
    修正後:    LinkSection=            OpMachine, …, DevTPMStatus, …, OpWLAN_ErpRet                ※DevTPMStatusを追加

    [DevUserAuthentication]
    修正前:    DefaultItem=            DevUserAuthentic_Dis
            ↓
    修正後:    DefaultItem=            DevUserAuthentic_GeneralSV

    [EasySet] 
    修正前:    Count=          7
    修正前:    Order=          ES_001,ES_002,ES_003,ES_004,ES_005,ES_006,ES_007
            ↓
    修正後:    ;// Count=          7
    修正後:    ;// Order=          ES_001,ES_002,ES_003,ES_004,ES_005,ES_006,ES_007
    修正後:    Count=          4
    修正後:    Order=          ES_001,ES_002,ES_003,ES_004

    [OutputMethod] 
    修正前:    Count=          6
    修正前:    Order=          NormalPrint,SecurePrint,SaveBox,SaveBoxAndPrint,ProofAndPrint,TouchAndPrint
    修正前:    SubSection=             NormalPrint,SecurePrint,SaveBox,SaveBoxAndPrint,WaitMode,ProofAndPrint,TouchAndPrint
            ↓
    修正後:    Count=          7
    修正後:    Order=          NormalPrint,SecurePrint,SaveBox,SaveBoxAndPrint,ProofAndPrint,TouchAndPrint,PKICardPrint
    修正後:    SubSection=             NormalPrint,SecurePrint,SaveBox,SaveBoxAndPrint,WaitMode,ProofAndPrint,TouchAndPrint,PKICardPrint

    追加: [PKICardPrint]                          ※以下、[TouchAndPrint]の下に追加

    追加: dmID=           18                  この行を使用する（2014.10.21から）
    追加: PJLValue=           NOSET

    追加: [ICCardUsed]                            ※以下、[UserAuthentic_NoPassWord]の下に追加
    追加: Count=          2
    追加: Order=          ICCardUsedOFF,ICCardUsedON
    追加: DefaultItem=            ICCardUsedON
    """
    if fName.lower() == "uisetup.ini":
        TxtFile = TxtFileHandle.TxtFileHandle()
        generator = TxtFile.ReadTxtFile(targetFile)

        toBeWritten = ""
        isFind = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("Ver_UISetup.*\d(0)0", line):
                line = re.sub("(Ver_UISetup.*?\d)0(0)", lambda mc: mc.group(1) + '1' + mc.group(2), line)
                isFind = True

            if re.search("Order.*DevUserAuthentication", line) and ";//" not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                toBeWritten += line.replace("DevUserAuthentication", "DevTPMStatus")
                toBeWritten += ";// " + theComment + " -E\r\n"
                # isFind = True
                continue

            if re.search("LinkSection.*OpWLAN_ErpRet", line) and ";//" not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                toBeWritten += line.replace("OpWLAN_ErpRet", "OpWLAN_ErpRet,DevTPMStatus")
                toBeWritten += ";// " + theComment + " -E\r\n"
                # isFind = True
                continue

            if re.search("DefaultItem.*DevUserAuthentic_Dis", line) and ";//" not in line:
                toBeWritten += ";// " + theComment + " -S\r\n"
                toBeWritten += ";// " + line
                toBeWritten += line.replace("DevUserAuthentic_Dis", "DevUserAuthentic_GeneralSV")
                toBeWritten += ";// " + theComment + " -E\r\n"
                isFind = True
                continue

            # [EasySet]
            # 他の関数処理

            # [OutputMethod]
            # 他の関数処理

            # [TouchAndPrint]
            # 他の関数処理

            # [ICCardUsed]
            # 他の関数処理

            toBeWritten += line

        if doReplace and isFind:
            TxtFile.WriteTxtFile(toBeWritten)
            print("replced file: {}".format(targetFile))

    """
    7. Version.ini

    [Version]
    修正前:    Ver_driver=         a.b.c.0
            ↓
    修正後:    Ver_driver=         a.b.c.OSW1_01
    """
    if fName.lower() == "version.ini":
        TxtFile = TxtFileHandle.TxtFileHandle()
        generator = TxtFile.ReadTxtFile(targetFile)

        toBeWritten = ""
        isFind = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("(Ver_driver.*\d.\d.\d.)0", line):
                line = re.sub("(Ver_driver.*\d.\d.\d.)0", lambda mc: mc.group(1) + "OSW1_01", line)
                isFind = True

            toBeWritten += line

        if doReplace and isFind:
            TxtFile.WriteTxtFile(toBeWritten)
            print("replced file: {}".format(targetFile))

    """
    9. *******.inf or ********.unf (PCL/PS共通)

    [Version]
    修正前:    DriverVer=          mm/dd/yyyy,a.b.c.0
            ↓
    修正後:    DriverVer=          mm/dd/yyyy,a.b.c.1

    [KOAYC_COPY] or [G_FILES]
    削除: ******_E.KMP
    削除: ******_F.KMP
    削除: ******_G.KMP

    [SourceDisksFiles] or [SourceDisksFiles.amd64]
    削除: ******_E.KMP = 4
    削除: ******_F.KMP = 4
    削除: ******_G.KMP = 4
    """
    if fExt.lower() == "inf":
        TxtFile = TxtFileHandle.TxtFileHandle()
        generator = TxtFile.ReadTxtFile(targetFile)

        toBeWritten = ""
        isFind = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("(DriverVer.*\d\.\d\.\d\.)0", line):
                line = re.sub("(DriverVer.*\d\.\d\.\d\.)0", lambda mc: mc.group(1) + "OSW1_01", line)
                isFind = True

            for s in ["_E", "_F", "_G", "_L", "_M", "_N", "_S", "_T", "_U"]:
                if re.search("^KOAY.*{0}\.KMP".format(s), line) and ";//" not in line:
                    line = ""
                    isFind = True

            toBeWritten += line

        if doReplace and isFind:
            TxtFile.WriteTxtFile(toBeWritten)
            print("replced file: {}".format(targetFile))

    """
    10. KMPファイル （2014.12.17 張麟補足）
                
    [Version]
    修正前:    version=            "a.b.c.0"
            ↓
    修正後:    version=            "a.b.c.OSW1_01"
        ※即ちVersion.iniの値と同じ

    KMPフォルダ中、下記不要なKMPファイルを削除：
    削除: ******_E.KMP
    削除: ******_F.KMP
    削除: ******_G.KMP
    """
    if fExt.lower() == "kmp":
        TxtFile = TxtFileHandle.TxtFileHandle()
        generator = TxtFile.ReadTxtFile(targetFile)

        toBeWritten = ""
        isFind = False

        if generator == "":
            print("Error Read file: {0}".format(fPathName))
            return

        for line in generator:
            if re.search("(version.*\d\.\d\.\d\.)0", line):
                line = re.sub("(version.*\d\.\d\.\d\.)0", lambda mc: mc.group(1) + "OSW1_01", line)
                isFind = True

            toBeWritten += line

        if doReplace and isFind:
            TxtFile.WriteTxtFile(toBeWritten)
            print("replced file: {}".format(targetFile))

        # [KMP削除]
        # 他の関数処理

def deleteFolderFile():
    # delete folders
    tup = os.walk(targetFolder)
    for root, dirs, files in tup:
        if "XPS_GPD" in root.split("\\")[-1]:
            try:
                shutil.rmtree(root)
                print("Remove folder: " + root)
            except WindowsError:
                print("oops...")

        for l in ["DE", "ES", "FR", "IT", "JA", "KO", "ZH-CN", "ZH-TW"]: # without "EN"
            if root.split("\\")[-1] == l:
                try:
                    shutil.rmtree(root)
                    print("Remove folder: " + root)
                except WindowsError:
                    print("oops...")

    # delete files
    tup = os.walk(targetFolder)
    for root, dirs, files in tup:
        for f in files:
            if f.split(".")[-1].lower() == "kmp":
                for s in ["_E", "_F", "_G", "_L", "_M", "_N", "_S", "_T", "_U"]:
                    if re.search("KOAY.*{0}\.KMP".format(s), f):
                        f = os.path.join(root, f)
                        try:
                            os.remove(f)
                            print("Remove file: " + f)
                        except WindowsError:
                            print("oops...")

    print("FOLDERS and FILES are deleted")
    print("Please make a commit before next step")
    print("")
    print("If you are ready to change file content, press ENTER...")

    try:
        input()
    except:
        pass

def isTargetFile(FileName):
    sufix = os.path.splitext(FileName)[1][1:]

    if sufix.upper() in fExt:
        return True

    else:
        return False

if __name__ == '__main__':
    deleteFolderFile()
    tup = os.walk(targetFolder)
    for root, dirs, files in tup:
        for f in files:
            if isTargetFile(f):
                targetFile = os.path.join(root, f)
                processFile(targetFile)