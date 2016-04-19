
; ControlSend("INITOKPD2", "", "[CLASS:Button; INSTANCE:2]", "{Enter}")

ControlClick("INITOKPD2", "", '', "", 1, 88, 17)

Global $TYPE_FOLDER = 1
Global $TYPE_FILE   = 2

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

$curPath = @WorkingDir
$topFolder = $curPath & "\..\.."

;$OWN_PCL_KPD_PTR = $topFolder & "\Driver\Model\" & $PDL &"\CUSTOM\KPD\_PCLXL\JA"
;$OWN_PCL_KPD_FA  = $topFolder & "\Driver\Model\" & $PDL &"FA\CUSTOM\KPD\_PCLXL\JA"

$l = GetNames("E:\Git_Mine\tools-lite\au3", 2)

ConsoleWrite($l[0] & @CRLF)

;MsgBox(0, "MsgBox", $PCL_KPD_Folder)



