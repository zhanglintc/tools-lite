
; ControlSend("INITOKPD2", "", "[CLASS:Button; INSTANCE:2]", "{Enter}")

; ControlClick("INITOKPD2", "", '', "", 1, 88, 17)

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

Func GetNames($givenPath, $type)
    ; Assign a Local variable the search handle of all files in the current directory.
    Local $hSearch = FileFindFirstFile($givenPath & "\*.*")

    ; Check if the search was successful, if not display a message and return False.
    If $hSearch = -1 Then
        MsgBox($MB_SYSTEMMODAL, "", "Error: No files/directories matched the search pattern.")
        Return False
    EndIf

    ; Assign a Local variable the empty string which will contain the files names found.
    Local $sFileName = "", $iCount = 0

    While 1
        $sFileName = FileFindNextFile($hSearch)
        ; If there is no more file matching the search.
        If @error Then ExitLoop

        If $type = $TYPE_FILE And StringInStr($sFileName, ".") Then
            $iCount += 1
        ElseIf $type = $TYPE_FOLDER And Not StringInStr($sFileName, ".") Then
            $iCount += 1
        EndIf
    WEnd

    ; Close the search handle.
    FileClose($hSearch)

    Local $aFiles[$iCount]
    $hSearch = FileFindFirstFile($givenPath & "\*.*")

    If $hSearch = -1 Then
        MsgBox($MB_SYSTEMMODAL, "", "Error: No files/directories matched the search pattern.")
        Return False
    EndIf

    $sFileName = ""
    $iCount = 0

    While 1
        $sFileName = FileFindNextFile($hSearch)
        ; If there is no more file matching the search.
        If @error Then ExitLoop

        If $type = $TYPE_FILE And StringInStr($sFileName, ".") Then
            $aFiles[$iCount] = $sFileName
            $iCount += 1
        ElseIf $type = $TYPE_FOLDER And Not StringInStr($sFileName, ".") Then
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

$INI2KPD_FOLDER = @WorkingDir
$TOP_FOLDER = StringReplace($INI2KPD_FOLDER, "\InitoKPD\RELEASE(NewKey)", "")
$MODEL_FOLDER = $TOP_FOLDER & "\Driver\Model"

LoadModels($MODEL_FOLDER)

ControlSetText("INITOKPD2", "", "Edit1", $OWN_PTR)
Sleep(100)
ControlSend("INITOKPD2", "", "Button2", "{SPACE}")

ControlSetText("INITOKPD2", "", "Edit2", $MODEL_FOLDER & "\" & $OWN_PTR & "\CUSTOM\INI\_PCLXL")
ControlSetText("INITOKPD2", "", "Edit3", $MODEL_FOLDER & "\" & $OWN_PTR & "\CUSTOM\INI")

; 填写各个 KPD 名字
LoadKPDs($MODEL_FOLDER & "\" & $OWN_PTR & "\CUSTOM\KPD\_PCLXL\JA")
ControlSetText("INITOKPD2", "", "Edit4", $DeviceCaps)
ControlSetText("INITOKPD2", "", "Edit5", $Command)
ControlSetText("INITOKPD2", "", "Edit6", $Cst)
ControlSetText("INITOKPD2", "", "Edit7", $Version)
ControlSetText("INITOKPD2", "", "Edit8", $Phonebook)

; 进入 Output 设置
ControlSend("INITOKPD2", "", "Button14", "{SPACE}") ; 点击 New
Sleep(100)
ControlSetText("Folder Name Registration", "", "Edit1", "KPD") ; 填写 Folder　Name
ControlSetText("Folder Name Registration", "", "Edit2", $MODEL_FOLDER & "\" & $OWN_PTR & "\CUSTOM\KPD") ; 填写 Top Folder

; 修改Folder Item => PDL
ControlSend("Folder Name Registration", "", "ListBox2", "{HOME}") ; 到顶
ControlSend("Folder Name Registration", "", "ListBox2", "{DOWN}") ; 下移一位到 PDL
ControlSend("Folder Name Registration", "", "Button9", "{SPACE}") ; 打开 PDL 设置
Sleep(100)
ControlSetText("PDL Information", "", "Edit2", "_PCLXL") ; 填写内容
ControlSend("PDL Information", "", "Button3", "{SPACE}") ; 点击 Set
ControlSend("PDL Information", "", "Button1", "{SPACE}") ; 点击 OK
ControlSend("Folder Name Registration", "", "Button6", "{SPACE}") ; 点击 Add

ControlSend("Folder Name Registration", "", "ListBox2", "{HOME}") ; 到顶
ControlSend("Folder Name Registration", "", "ListBox2", "{DOWN}") ; 下移一位到 PDL
ControlSend("Folder Name Registration", "", "ListBox2", "{DOWN}") ; 下移一位到 Language Folder
ControlSend("Folder Name Registration", "", "Button6", "{SPACE}") ; 点击 Add

ControlSend("Folder Name Registration", "", "Button1", "{SPACE}") ; 点击 OK






