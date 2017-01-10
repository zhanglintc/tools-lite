#RequireAdmin

#include <WinAPIProc.au3>

Global $TITLE_VER = "MakeIT2_NoXPS -- v0.1"
Global $Author    = "ZhangLin"

Global $TYPE_FOLDER = 1
Global $TYPE_FILE   = 2

Global $OWN_PTR = ""
Global $OWN_FA = ""
Global $GEN_PTR = ""
Global $GEN_FA = ""
Global $PKI_PTR = ""

Global $DeviceCaps = ""
Global $Command = ""
Global $Cst = ""
Global $Version = ""
Global $Phonebook = ""

Func IsFolder($filePath)
    $Attrib = FileGetAttrib($filePath)
    If StringInStr($Attrib, "D") Then
        Return True
    EndIf

    Return False
EndFunc

Func IsFile($filePath)
    $Attrib = FileGetAttrib($filePath)
    If Not StringInStr($Attrib, "D") Then
        Return True
    EndIf

    Return False
EndFunc

Func GetNames($givenPath, $type)
    ; Assign a Local variable the search handle of all files in the current directory.
    Local $hSearch = FileFindFirstFile($givenPath & "\*.*")

    ; Check if the search was successful, if not display a message and return False.
    If $hSearch = -1 Then
        MsgBox(0, $TITLE_VER, "Error: No files/directories matched the search pattern.")
        Return False
    EndIf

    ; Assign a Local variable the empty string which will contain the files names found.
    Local $sFileName = "", $iCount = 0

    While 1
        $sFileName = FileFindNextFile($hSearch)
        ; If there is no more file matching the search.
        If @error Then ExitLoop

        If $type = $TYPE_FILE And IsFile($givenPath & "\" & $sFileName) Then
            $iCount += 1
        ElseIf $type = $TYPE_FOLDER And IsFolder($givenPath & "\" & $sFileName) Then
            $iCount += 1
        EndIf
    WEnd

    ; Close the search handle.
    FileClose($hSearch)

    Local $aFiles[$iCount]
    $hSearch = FileFindFirstFile($givenPath & "\*.*")

    If $hSearch = -1 Then
        MsgBox(0, $TITLE_VER, "Error: No files/directories matched the search pattern.")
        Return False
    EndIf

    $sFileName = ""
    $iCount = 0

    While 1
        $sFileName = FileFindNextFile($hSearch)
        ; If there is no more file matching the search.
        If @error Then ExitLoop

        If $type = $TYPE_FILE And IsFile($givenPath & "\" & $sFileName) Then
            $aFiles[$iCount] = $sFileName
            $iCount += 1
        ElseIf $type = $TYPE_FOLDER And IsFolder($givenPath & "\" & $sFileName) Then
            $aFiles[$iCount] = $sFileName
            $iCount += 1
        EndIf
    WEnd

    FileClose($hSearch)
    Return $aFiles
EndFunc

Func LoadModels($TARGET)
    $MODEL_LIST = GetNames($TARGET, $TYPE_FOLDER)

    For $MODEL In $MODEL_LIST
        If StringInStr($MODEL, "-") Then
            If StringInStr($MODEL, "FA") Then
                $GEN_FA = $MODEL
            Else
                $GEN_PTR = $MODEL
            EndIf
        ElseIf StringInStr($MODEL, "PKI") Then
            $PKI_PTR = $MODEL
        Else
            If StringInStr($MODEL, "FA") Then
                $OWN_FA = $MODEL
            Else
                $OWN_PTR = $MODEL
            EndIf
        EndIF
    Next
EndFunc

Func LoadKPDs($TARGET)
    $DeviceCaps = ""
    $Command = ""
    $Cst = ""
    $Version = ""
    $Phonebook = ""

    $KPD_LIST = GetNames($TARGET, $TYPE_FILE)

    For $KPD In $KPD_LIST
        If     StringInStr($KPD, "D.KPD") Then
            $DeviceCaps = $KPD
        ElseIf StringInStr($KPD, "M.KPD") Then
            $Command = $KPD
        ElseIf StringInStr($KPD, "C.KPD") Then
            $Cst = $KPD
        ElseIf StringInStr($KPD, "_.KPD") Then
            $Version = $KPD
        ElseIf StringInStr($KPD, "V.KPD") Then
            $Phonebook = $KPD
        EndIF
    Next
EndFunc

If Not WinExists("INITOKPD2") Then
    MsgBox(0, $TITLE_VER, "No iniToKPD2.exe is running.")
    Exit
EndIf

; 新建工程
WinActivate("INITOKPD2")
Send("!fn")
Sleep(100)

; 不保存结果
If WinExists("INITOKPD2", "Do you save a file?") Then
    ControlSend("INITOKPD2", "", "Button2", "{SPACE}")
EndIf

$INI2KPD_PID = WinGetProcess("INITOKPD2")
$INI2KPD_FOLDER = _WinAPI_GetProcessWorkingDirectory($INI2KPD_PID)
$TOP_FOLDER = StringReplace($INI2KPD_FOLDER, "\InitoKPD\RELEASE(NewKey)", "")
$MODEL_FOLDER = $TOP_FOLDER & "\Driver\Model"

Local $MODELs[5]
LoadModels($MODEL_FOLDER)
$MODELs[0] = $OWN_PTR
$MODELs[1] = $OWN_FA
$MODELs[2] = $GEN_PTR
$MODELs[3] = $GEN_FA
$MODELs[4] = $PKI_PTR

For $MODEL In $MODELs
    If $MODEL == "" Then
        ContinueLoop
    EndIf

    ; 填写机种名
    ControlSetText("INITOKPD2", "", "Edit1", $MODEL)
    Sleep(100)
    ControlSend("INITOKPD2", "", "Button2", "{SPACE}")

    ; 选择以空白模式添加新机种
    Sleep(100)
    If WinExists("IniToBin Model Add") Then
        ControlSend("IniToBin Model Add", "", "Button3", "{SPACE}")
        ControlSend("IniToBin Model Add", "", "Button1", "{SPACE}")
    EndIf

    Local $PDLs[3]
    If $MODEL = $OWN_PTR Or $MODEL = $GEN_PTR Then
        $PDLs[0] = "_PCLXL"
        $PDLs[1] = "_PS"
        $PDLs[2] = ""
    ElseIf $MODEL = $OWN_FA Or $MODEL = $GEN_FA Then
        $PDLs[0] = "_PCLXL"
        $PDLs[1] = ""
        $PDLs[2] = ""
    ElseIf $MODEL = $PKI_PTR Then
        $PDLs[0] = "_PCLXL"
        $PDLs[1] = "_PS"
        $PDLs[2] = ""
    EndIf

    For $PDL in $PDLs
        ; 设置 PDL 种类
        If     $PDL = "_PCLXL" Then
            ControlSend("INITOKPD2", "", "ComboBox2", "{HOME}")

        ElseIf $PDL = "_PS" Then
            ControlSend("INITOKPD2", "", "ComboBox2", "{HOME}")
            ControlSend("INITOKPD2", "", "ComboBox2", "{DOWN}")

        ElseIf $PDL = "_XPS_GPD" Then
            ControlSend("INITOKPD2", "", "ComboBox2", "{HOME}")
            ControlSend("INITOKPD2", "", "ComboBox2", "{DOWN}")
            ControlSend("INITOKPD2", "", "ComboBox2", "{DOWN}")

        Else
            ContinueLoop
        EndIf

        ; 填写 ini 地址
        ControlSetText("INITOKPD2", "", "Edit2", $MODEL_FOLDER & "\" & $MODEL & "\CUSTOM\INI\" & $PDL)
        ControlSetText("INITOKPD2", "", "Edit3", $MODEL_FOLDER & "\" & $MODEL & "\CUSTOM\INI")

        ; 填写各个 KPD 名字
        LoadKPDs($MODEL_FOLDER & "\" & $MODEL & "\CUSTOM\KPD\" & $PDL & "\EN")
        ControlSetText("INITOKPD2", "", "Edit4", $DeviceCaps)
        ControlSetText("INITOKPD2", "", "Edit5", $Command)
        ControlSetText("INITOKPD2", "", "Edit6", $Cst)
        ControlSetText("INITOKPD2", "", "Edit7", $Version)
        ControlSetText("INITOKPD2", "", "Edit8", $Phonebook)

        ; 进入 Output 设置
        ControlSend("INITOKPD2", "", "Button14", "{SPACE}") ; 点击 New
        Sleep(100)
        ControlSetText("Folder Name Registration", "", "Edit1", "KPD") ; 填写 Folder　Name
        ControlSetText("Folder Name Registration", "", "Edit2", $MODEL_FOLDER & "\" & $MODEL & "\CUSTOM\KPD") ; 填写 Top Folder

        ; 修改Folder Item => PDL
        ControlSend("Folder Name Registration", "", "ListBox2", "{HOME}") ; 到顶
        ControlSend("Folder Name Registration", "", "ListBox2", "{DOWN}") ; 下移一位到 PDL
        ControlSend("Folder Name Registration", "", "Button9", "{SPACE}") ; 打开 PDL 设置
        Sleep(100)
        ControlSetText("PDL Information", "", "Edit2", $PDL) ; 填写内容
        ControlSend("PDL Information", "", "Button3", "{SPACE}") ; 点击 Set
        ControlSend("PDL Information", "", "Button1", "{SPACE}") ; 点击 OK
        ControlSend("Folder Name Registration", "", "Button6", "{SPACE}") ; 点击 Add

        ControlSend("Folder Name Registration", "", "ListBox2", "{HOME}") ; 到顶
        ControlSend("Folder Name Registration", "", "ListBox2", "{DOWN}") ; 下移一位到 PDL
        ControlSend("Folder Name Registration", "", "ListBox2", "{DOWN}") ; 下移一位到 Language Folder
        ControlSend("Folder Name Registration", "", "Button6", "{SPACE}") ; 点击 Add

        ControlSend("Folder Name Registration", "", "Button1", "{SPACE}") ; 点击 OK
    Next
Next

MsgBox(0, $TITLE_VER, "IT2 Project has been created.")

