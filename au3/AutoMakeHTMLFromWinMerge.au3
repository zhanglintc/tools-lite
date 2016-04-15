#include <Array.au3>
#include <File.au3>
#include <FileConstants.au3>
#include <GUIConstantsEx.au3>
#include <GuiListView.au3>
#include <ListViewConstants.au3>
#include <EditConstants.au3>
#include <GuiEdit.au3>
#include <StringConstants.au3>
#include <Timers.au3>

; Changelog:
; v1.0 初版做成(NB 的初版) by FangJun
; v1.1 解决路径中含有九语言字样(如 IT, DE 等)导致成果物中出现 IT, DE 字样以及生成失败 by ZhangLin
; v1.2 增加默认文件名处理(当无法匹配任何规则时), 大幅优化生成速度(时间缩减 60%), 添加 html 默认生成路径 by YanBin & ZhangLin
; v1.3 ①自动关闭因为编码错误出现的对话框以便保证程序正常运行 ②将生成的文件名中的减号"-"统一修改为下划线"_"(否则Excel导入时会报错) by ZhangLin

CreateGUI()

Func CreateGUI()
    Global $Paused
    HotKeySet("!c", "TogglePause")
    HotKeySet("!x", "Terminate")
    Local $hMainGUI = GUICreate("AutoMakeHTML v1.3", 600, 300)
    GUICtrlCreateLabel("Different File List", 10, 10)
    Global $idListview = GUICtrlCreateListView("No. | FileName | Path ", 10, 30, 580, 150)
    GUICtrlSetState(-1, $GUI_DROPACCEPTED)
    GUICtrlCreateLabel("HTML Store Path", 10, 190)
    Global $idFilePath = GUICtrlCreateInput("", 110, 185, 350, BitAND($ES_READONLY, $ES_AUTOHSCROLL, $ES_LEFT))
    Local $selectButton = GUICtrlCreateButton("Select", 470, 185, 100)
    Local $readButton = GUICtrlCreateButton("Read Diff List", 10, 220, 100)
    Local $genHTMLButton = GUICtrlCreateButton("Create Html Files", 130, 220)
    ; Local $testButton = GUICtrlCreateButton("Test", 290, 220, 100)
    Global $DECheckbox = GUICtrlCreateCheckbox("DE", 10, 260)
    Global $ENCheckbox = GUICtrlCreateCheckbox("EN", 60, 260)
    Global $ESCheckbox = GUICtrlCreateCheckbox("ES", 110, 260)
    Global $FRCheckbox = GUICtrlCreateCheckbox("FR", 160, 260)
    Global $ITCheckbox = GUICtrlCreateCheckbox("IT", 210, 260)
    Global $JACheckbox = GUICtrlCreateCheckbox("JA", 260, 260)
    Global $KOCheckbox = GUICtrlCreateCheckbox("KO", 310, 260)
    Global $CNCheckbox = GUICtrlCreateCheckbox("CN", 360, 260)
    Global $TWCheckbox = GUICtrlCreateCheckbox("TW", 410, 260)
    GUICtrlCreateLabel("unuse language", 460, 260)
    GUISetState(@SW_SHOW, $hMainGUI)

    While 1
        Switch GUIGetMsg()
            Case $GUI_EVENT_CLOSE
               ; MsgBox(0, "Exit Message", "You selected CLOSE! Exiting...")
               ExitLoop
            Case $readButton
                ReadDiffList()
            Case $genHTMLButton
                GenHtmls()
            Case $selectButton
                PathSelect()
            ; Case $testButton
                ; Test()
        EndSwitch
    WEnd
EndFunc

Func Test()
    ; _FileCreate("E:\work\AutoHTMLFromWinMerge\txt.txt")
    $szTmpFPath = StringStripWS(_GUICtrlListView_GetItemText($idListview, 1, 2), 8)
    If StringRegExp($szTmpFPath, ".+\\Model\\(.+-.+)\\.+") Then
        $szTmpFPath = $szTmpFPath & "yes"
    EndIf
    MsgBox(0, "ff", $szTmpFPath)

EndFunc

Func TogglePause()
    $Paused = Not $Paused
    While $Paused
        Sleep(100)
        ToolTip('Auto Create Html file Script is "Paused" press "Alt+C" to Run.', 2)
    WEnd
    ToolTip("")
EndFunc

Func Terminate()
    $rlt = MsgBox(4, "Quit", "Sure to quit.")
    if $rlt == 6 Then
        Exit 0
    EndIf
EndFunc

Func GenHtmls()
    Local $hWnd = WinGetHandle("[CLASS:WinMergeWindowClassW]")
    If @error Then
        MsgBox($MB_SYSTEMMODAL, "", "An error occurred when trying to retrieve the window handle of WinMerge.")
        Return
    EndIf

    $curFilePath = _GUICtrlEdit_GetText($idFilePath)
    if $curFilePath == "" Then
        $curFilePath = @WorkingDir ; 如果没有指定生成路径， 则默认生成到脚本当前路径
    EndIf

    Local $hStarttime = _Timer_Init()

    $curTime = @YEAR & @MON & @MDAY & @HOUR & @MIN & @SEC
    $curFilePath = $curFilePath & "\" & $curTime
    If not DirCreate($curFilePath) Then
        MsgBox($MB_SYSTEMMODAL, "Error", "Create html store error!")
        Return
    EndIf
    If not _FileCreate($curFilePath & "\" & $curTime & "_log.txt") Then
        MsgBox($MB_SYSTEMMODAL, "Error", "Create log file error!")
        Return
    EndIf

    Local $hLogFileOpen = FileOpen($curFilePath & "\" & $curTime & "_log.txt", $FO_APPEND)
    If $hLogFileOpen = -1 Then
        MsgBox($MB_SYSTEMMODAL, "", "An error occurred when open the Log.")
        Return
    EndIf

    ; FileWriteLine($hLogFileOpen, "The below files did not create html:")

    ; Display the handle of the Notepad window.
    ; MsgBox($MB_SYSTEMMODAL, "", $hWnd)

    $listCount = _GUICtrlListView_GetItemCount($idListview)
    If WinExists("[CLASS:WinMergeWindowClassW]") Then
        WinActivate($hWnd)
        WinWaitActive("[CLASS:WinMergeWindowClassW]")
        Send("{HOME}")
        For $i = 0 To $listCount-1 Step 1
            $szTmpFName = StringStripWS(_GUICtrlListView_GetItemText($idListview, $i, 1), 8)
            $szOrgFName = $szTmpFName
            $szTmpFPath = StringStripWS(_GUICtrlListView_GetItemText($idListview, $i, 2), 8)
            if (StringInStr($szTmpFPath, "\RAST") Or StringInStr($szTmpFPath, "\_RAST") Or StringInStr($szTmpFPath, "\_PCL") Or StringInStr($szTmpFPath, "\PCL")  Or StringInStr($szTmpFPath, "_PCL_")) and (0=StringInStr($szTmpFPath, "FA\")) Then
                $szTmpFName = $szTmpFName & "_PCL"
            EndIf
            if StringInStr($szTmpFPath, "\PS") Or StringInStr($szTmpFPath, "\_PS")  Or StringInStr($szTmpFPath, "_PS_")  Then
                $szTmpFName = $szTmpFName & "_PS"
            EndIf
            if StringInStr($szTmpFPath, "\XPS") Or StringInStr($szTmpFPath, "\_XPS")  Or StringInStr($szTmpFPath, "_XPS_")  Then
                $szTmpFName = $szTmpFName & "_XPS"
            EndIf
            ; if (StringInStr($szTmpFPath, "\PCLXL") Or StringInStr($szTmpFPath, "\_PCLXL")) And StringInStr($szTmpFPath, "FA\")  Then
            ;     $szTmpFName = $szTmpFName & "_FAX"
            ; EndIf

            ; if (StringInStr($szTmpFPath, "\PCLXL") Or StringInStr($szTmpFPath, "\_PCLXL")) And 0=StringInStr($szTmpFPath, "FA\")  Then
            ;     $szTmpFName = $szTmpFName & "_PCL"
            ; EndIf

            if StringInStr($szTmpFPath, "FA\") Then
                $szTmpFName = $szTmpFName & "_FAX"
            EndIf
            if StringInStr($szTmpFPath, "\DE\") Then
                $szTmpFName = $szTmpFName & "_DE"
            EndIf
            if StringInStr($szTmpFPath, "\EN\") Then
                $szTmpFName = $szTmpFName & "_EN"
            EndIf
            if StringInStr($szTmpFPath, "\ES\") Then
                $szTmpFName = $szTmpFName & "_ES"
            EndIf
            if StringInStr($szTmpFPath, "\FR\") Then
                $szTmpFName = $szTmpFName & "_FR"
            EndIf
            if StringInStr($szTmpFPath, "\IT\") Then
                $szTmpFName = $szTmpFName & "_IT"
            EndIf
            if StringInStr($szTmpFPath, "\JA\") Then
                $szTmpFName = $szTmpFName & "_JA"
            EndIf
            if StringInStr($szTmpFPath, "\KO\") Then
                $szTmpFName = $szTmpFName & "_KO"
            EndIf
            if StringInStr($szTmpFPath, "\ZH-CN\") Then
                $szTmpFName = $szTmpFName & "_ZN"
            EndIf
            if StringInStr($szTmpFPath, "\ZH-TW\") Then
                $szTmpFName = $szTmpFName & "_ZW"
            EndIf
            if StringInStr($szTmpFPath, "\Win2kXP") Or StringInStr($szTmpFPath, "\Win_x86") Or StringInStr($szTmpFPath, "\WinLH32") Then
                $szTmpFName = $szTmpFName & "_32"
            EndIf
            if StringInStr($szTmpFPath, "\Win64") Or StringInStr($szTmpFPath, "\Win_x64") Or StringInStr($szTmpFPath, "\WinLH64") Then
                $szTmpFName = $szTmpFName & "_64"
            EndIf
            if StringInStr($szTmpFPath, "\Mono")  Or StringInStr($szTmpFPath, "_Mono_") Then
                $szTmpFName = $szTmpFName & "_M"
            EndIf

            ; MsgBox($MB_SYSTEMMODAL, $szTmpFName, $szTmpFPath)
            ; if StringInStr($szTmpFPath, "PKI") Then
            if StringRegExp($szTmpFPath, "\\Model\\(.+PKI)\\") Then
                $szTmpFName = $szTmpFName & "_P"
            ; ElseIf StringRegExp($szTmpFPath, ".+\\Model\\(.+-.+)\\.+") or StringInStr($szTmpFPath, "_Gen") Then
            ElseIf StringRegExp($szTmpFPath, ".+\\Model\\(.+-.+)\\.+") Then
                $szTmpFName = $szTmpFName & "_G"
            Else
                $szTmpFName = $szTmpFName & "_O"
            EndIf

            If _IsChecked($DECheckbox) And StringInStr($szTmpFPath, "\DE\") Then
                FileWriteLine($hLogFileOpen, $szTmpFPath & $szOrgFName & " is not created => DE")
                Send("{DOWN}")
            ElseIf _IsChecked($ENCheckbox) And StringInStr($szTmpFPath, "\EN\") Then
                FileWriteLine($hLogFileOpen, $szTmpFPath & $szOrgFName & " is not created => EN")
                Send("{DOWN}")
            ElseIf _IsChecked($ESCheckbox) And StringInStr($szTmpFPath, "\ES\") Then
                FileWriteLine($hLogFileOpen, $szTmpFPath & $szOrgFName & " is not created => ES")
                Send("{DOWN}")
            ElseIf _IsChecked($FRCheckbox) And StringInStr($szTmpFPath, "\FR\") Then
                FileWriteLine($hLogFileOpen, $szTmpFPath & $szOrgFName & " is not created => FR")
                Send("{DOWN}")
            ElseIf _IsChecked($ITCheckbox) And StringInStr($szTmpFPath, "\IT\") Then
                FileWriteLine($hLogFileOpen, $szTmpFPath & $szOrgFName & " is not created => IT")
                Send("{DOWN}")
            ElseIf _IsChecked($JACheckbox) And StringInStr($szTmpFPath, "\JA\") Then
                FileWriteLine($hLogFileOpen, $szTmpFPath & $szOrgFName & " is not created => JA")
                Send("{DOWN}")
            ElseIf _IsChecked($KOCheckbox) And StringInStr($szTmpFPath, "\KO\") Then
                FileWriteLine($hLogFileOpen, $szTmpFPath & $szOrgFName & " is not created => KO")
                Send("{DOWN}")
            ElseIf _IsChecked($CNCheckbox) And StringInStr($szTmpFPath, "\ZH-CN\") Then
                FileWriteLine($hLogFileOpen, $szTmpFPath & $szOrgFName & " is not created => CN")
                Send("{DOWN}")
            ElseIf _IsChecked($TWCheckbox) And StringInStr($szTmpFPath, "\ZH-TW\") Then
                FileWriteLine($hLogFileOpen, $szTmpFPath & $szOrgFName & " is not created => TW")
                Send("{DOWN}")
            Else
                Send("{ENTER}")
                While Not WinExists("WinMerge", "Diff Pane")
                    ; do noting here, just wait
                WEnd
                If WinExists("WinMerge", "無題") Then
                    Send("{ESC}") ; close the error window
                EndIf

                ; Sleep(1000) ; 任何强行人为设置的等待时间都是耍流氓, 特别是这种没有效果的等待 !
                Send("!tr")
                $szTmpFName = StringReplace($szTmpFName, "-", "_") ; change "-" to "_" in file name
                $curTmpFileStorePath = $curFilePath & "\" & $szTmpFName
                WinWaitActive("[CLASS:#32770]")
                If WinExists("[CLASS:#32770]") Then
                    Local $hFileDlgWnd = WinGetHandle("[CLASS:#32770]")
                    ControlSetText($hFileDlgWnd, "", "Edit1", $curTmpFileStorePath)
                    Send("!s")

                    While Not WinExists("WinMerge", "レポート生成に成功しました。") And Not WinExists("名前を付けて保存の確認")
                        ; do noting here, just wait
                    WEnd

                    Local $getWinForExist = ControlGetText("[CLASS:#32770]", "", "Button1")
                    Local $j = 0
                    While $getWinForExist <> "&Ok"
                        $j = $j + 1
                        Send("{ENTER}")
                        ControlSetText($hFileDlgWnd, "", "Edit1", $curTmpFileStorePath & "_" & $j)
                        Send("!s")
                        While Not WinExists("WinMerge", "レポート生成に成功しました。") And Not WinExists("名前を付けて保存の確認")
                            ; do noting here, just wait
                        WEnd
                        $getWinForExist = ControlGetText("[CLASS:#32770]", "", "Button1")
                    WEnd

                    if $j > 0 Then
                        FileWriteLine($hLogFileOpen, "file not match any rule: " & $curTmpFileStorePath & "_" & $j & ".htm")
                    EndIf

                    WinWaitActive("[CLASS:#32770]")
                    Send("{ENTER}")
                    ; Sleep(500) ; 任何强行人为设置的等待时间都是耍流氓, 特别是这种没有效果的等待 !
                    Send("{ESC}")
                Else
                    MsgBox($MB_SYSTEMMODAL, "", "Store dialog does not exist")
                EndIf
                ; Sleep(500) ; 任何强行人为设置的等待时间都是耍流氓, 特别是这种没有效果的等待 !
                Send("{DOWN}")
                if StringLen($szTmpFName) + 4 > 31 Then
                    FileWriteLine($hLogFileOpen, $szTmpFName & ".html file name len is over than 31 charachter.")
                EndIf
            EndIf
        Next
    Else
        MsgBox($MB_SYSTEMMODAL, "", "WinMerge does not exist")
    EndIf
    FileClose($hLogFileOpen)
    MsgBox($MB_SYSTEMMODAL, "", "Make Htmls Done!" & @CRLF & "Takes Time: " & Int((_Timer_Diff($hStarttime)) / 1000) & "s"  & @CRLF & @CRLF & $curFilePath)
EndFunc

Func PathSelect()
    Local Const $sMessage = "Select a folder"

    ; Display an open dialog to select a file.
    Local $sFileSelectFolder = FileSelectFolder($sMessage, "")
    If @error Then
        ; Display the error message.
        MsgBox($MB_SYSTEMMODAL, "", "No folder was selected.")
    Else
        ; Display the selected folder.
        ; MsgBox($MB_SYSTEMMODAL, "", "You chose the following folder:" & @CRLF & $sFileSelectFolder)
        GUICtrlSetData($idFilePath, $sFileSelectFolder)
    EndIf
EndFunc

Func _IsChecked($idControlID)
    Return BitAND(GUICtrlRead($idControlID), $GUI_CHECKED) = $GUI_CHECKED
EndFunc

Func ReadDiffList()
    _GUICtrlListView_DeleteAllItems ($idListview)
    $fileCount = 0

    $file = FileOpen("DiffFileList.txt", $FO_READ)

    ; Check if file opened for reading OK
    If $file = -1 Then
        MsgBox(48, "Error", "Unable to open file.")
        Exit
    EndIf

    ; Read in lines of text until the EOF is reached
    While 1
        $line = FileReadLine($file)
        If @error = -1 Then ExitLoop
        Dim $szDrive, $szDir, $szFName, $szExt
        _PathSplit($line, $szDrive, $szDir, $szFName, $szExt)
        $fileCount = $fileCount + 1
        $szFName = StringStripWS($szFName, 8)
        $itemTemp = $fileCount & " | " & $szFName & "_" & StringRight($szExt, 3) & " | " & $szDrive & $szDir
        GUICtrlCreateListViewItem($itemTemp, $idListview)
        ; MsgBox(0, "t", $szDir)
    Wend

    FileClose($file)
EndFunc
