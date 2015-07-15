VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "MyTool"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Dim curSheetName As String 'current operator sheet
Dim curHtmlFileName As String 'current file name
Dim lstHtmlFileName As String
Dim fileCount As Integer
Dim reg As New RegExp 'find wbs no in code comment
Dim conflictWBSDict


Private Sub clearAllSheets_Click()
    fileCount = 0
    deleteAllReportSheets
    clearSheetContent "表紙_集計"
End Sub

Sub InputCheck_Click()
    If MyTool.Cells(7, 16) = "Version更新" And Not MyTool.Cells(8, 16) = "バージョンのアップデート" Then
        MsgBox ("[Version更新]'s Comment should be [バージョンのアップデート]")
    End If
    If MyTool.Cells(7, 16) = "製品名対応" And MyTool.Cells(4, 17) = "" Then
        MsgBox ("When [製品名対応] is specified [機種名指定] can not be NULL")
    End If
    If MyTool.Cells(7, 16) = "ファイル名対応" And MyTool.Cells(3, 17) = "" Then
        MsgBox ("When [ファイル名対応] is specified [ファイル名指定] can not be NULL")
    End If
End Sub

Function dealSpecialForGenericINF(sheetName As String, rowNum As Integer)
    Set curSheetObj = Worksheets(sheetName)
    If curSheetObj.Cells(rowNum, 6) = "Diff" And (InStr(curSheetObj.Cells(rowNum, 2), "OEM URLS") > 0 Or InStr(curSheetObj.Cells(rowNum, 2), "%KM%") > 0) Then
        curSheetObj.Cells(rowNum, 7) = "●"
    End If
End Function

Function dealFileWithNoComment(sheetName As String, keyWord As String, strWBS As String, WBSType As String)

    Set curSheetObj = Worksheets(sheetName)
    curSheetObj.Select
    If Not curSheetObj.Cells(1, 8) = "" Then
        curSheetObj.Columns("G:G").Select
        Selection.Delete Shift:=xlToLeft
    End If
    
    projectListCount = curSheetObj.Range("B65536").End(xlUp).Row
    curSheetObj.Range("G1:G2").Select
    Selection.Copy
    curSheetObj.Cells(1, 8).Select
    ActiveSheet.Paste
    
    If (InStr(sheetName, "Localize_ini") > 0) Then
        For j = 3 To projectListCount
            If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), ";") < 1 Then
                curSheetObj.Cells(j, 7) = "●"
                curSheetObj.Cells(1, 7) = strWBS
            End If
            If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), ";") >= 1 Then
                curSheetObj.Cells(j, 7) = "※"
            End If
        Next
    Else
                
        For j = 3 To projectListCount
            If WBSType = "Version更新" Then
                If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), keyWord) Then
                    curSheetObj.Cells(j, 7) = "●"
                    curSheetObj.Cells(1, 7) = strWBS
                End If
            ElseIf WBSType = "WBS案件対応" Then
                If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), keyWord) < 1 Then
                    curSheetObj.Cells(j, 7) = "●"
                    curSheetObj.Cells(1, 7) = strWBS
                End If
            ElseIf WBSType = "製品名対応" Then
                If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), keyWord) < 1 And InStr(curSheetObj.Cells(j, 4), MyTool.Cells(4, 17)) > 0 Then
                    curSheetObj.Cells(j, 7) = "●"
                    curSheetObj.Cells(1, 7) = strWBS
                End If
            ElseIf WBSType = "ファイル名対応" Then
                If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), keyWord) < 1 And InStr(curSheetObj.Cells(j, 4), MyTool.Cells(3, 17)) > 0 Then
                    curSheetObj.Cells(j, 7) = "●"
                    curSheetObj.Cells(1, 7) = strWBS
                End If
            ElseIf WBSType = "Generic対応" Then
                If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), keyWord) < 1 And (InStr(curSheetObj.Cells(j, 4), MyTool.Cells(3, 17)) _
                Or InStr(curSheetObj.Cells(j, 4), MyTool.Cells(4, 17)) > 0 Or InStr(curSheetObj.Cells(j, 4), "DLMGREXE") > 0 Or InStr(curSheetObj.Cells(j, 4), "Generic") > 0) Then 'DLMGREXE is only for sub file
                    If InStr(curSheetObj.Cells(j, 4), ";") > 0 Then
                        curSheetObj.Cells(j, 7) = "※"
                        curSheetObj.Cells(1, 7) = strWBS
                    Else
                        curSheetObj.Cells(j, 7) = "●"
                        curSheetObj.Cells(1, 7) = strWBS
                    End If
                End If
                
                If (InStr(UCase(sheetName), "INF") > 0) Or (InStr(UCase(sheetName), "INF") > 0) Then
                    Call dealSpecialForGenericINF(sheetName, CInt(j))
                End If
            Else
                If curSheetObj.Cells(j, 6) = "Diff" Then
                    curSheetObj.Cells(j, 7) = "●"
                    curSheetObj.Cells(1, 7) = strWBS
                End If
            End If
        Next
    End If
    
End Function

Function dealFileWithComment(sheetName As String, strWBS As String, WBSType As String)
    
    Set curSheetObj = Worksheets(sheetName)
    curSheetObj.Select
    If Not curSheetObj.Cells(1, 8) = "" Then
        curSheetObj.Columns("G:G").Select
        Selection.Delete Shift:=xlToLeft
    End If
    
    projectListCount = curSheetObj.Range("B65536").End(xlUp).Row
    curSheetObj.Range("G1:G2").Select
    Selection.Copy
    curSheetObj.Cells(1, 8).Select
    ActiveSheet.Paste
    
    Dim isDiff As Boolean
    isDiff = False
    
    For j = 3 To projectListCount
    
        If curSheetObj.Cells(j, 6) = "Diff" And isDiff Then
            curSheetObj.Cells(j, 7) = "●"
        End If
        If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), strWBS) > 0 And InStr(curSheetObj.Cells(j, 4), "-S") > 0 Then
            curSheetObj.Cells(j, 7) = "※"
            curSheetObj.Cells(1, 7) = strWBS
            isDiff = True
        End If
        If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), strWBS) > 0 And InStr(curSheetObj.Cells(j, 4), "-E") > 0 Then
            curSheetObj.Cells(j, 7) = "※"
            isDiff = False
        End If
        
        If WBSType = "製品名対応" And curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), MyTool.Cells(4, 17)) > 0 Then
            curSheetObj.Cells(j, 7) = "●"
            curSheetObj.Cells(1, 7) = strWBS
        End If
        
        If WBSType = "ファイル名対応" And curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), MyTool.Cells(3, 17)) > 0 Then
            curSheetObj.Cells(j, 7) = "●"
            curSheetObj.Cells(1, 7) = strWBS
        End If
        
        If WBSType = "Generic対応" And curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), "Generic") > 0 Then
            curSheetObj.Cells(j, 7) = "※"
            curSheetObj.Cells(1, 7) = strWBS
        End If
        
        If WBSType = "Generic対応" And curSheetObj.Cells(j, 6) = "Diff" And (InStr(curSheetObj.Cells(j, 4), "OEMDriverFile1") > 0 Or InStr(curSheetObj.Cells(j, 4), "OEMConfigFile1") > 0) Then
            curSheetObj.Cells(j, 7) = "●"
            curSheetObj.Cells(1, 7) = strWBS
        End If
        
    Next
    
End Function

Function dealConflict(sheetName As String)
    Set curSheetObj = Worksheets(sheetName)
    curSheetObj.Select
    
    copyRowStart = 7
    
    For Each Key In conflictWBSDict
        curSheetObj.Range("G1:G2").Select
        Selection.Copy
        curSheetObj.Cells(1, copyRowStart).Select
        ActiveSheet.Paste
        curSheetObj.Cells(1, copyRowStart) = conflictWBSDict(Key)
        copyRowStart = copyRowStart + 1
    Next
    
    projectListCount = curSheetObj.Range("B65536").End(xlUp).Row
    
    curMarkRow = 6
    For j = 3 To projectListCount
        If curSheetObj.Cells(j, 6) = "Diff" Then
            If curMarkRow = 6 Then
                For Each Key In conflictWBSDict
                    If InStr(curSheetObj.Cells(j, 4), conflictWBSDict(Key)) > 0 And InStr(curSheetObj.Cells(j, 4), "-S") > 0 Then
                        curMarkRow = 6 + CInt(Key)
                        curSheetObj.Cells(j, curMarkRow) = "※"
                    End If
                Next
            Else
                If InStr(curSheetObj.Cells(j, 4), "-E") > 0 Then
                    curSheetObj.Cells(j, curMarkRow) = "※"
                    curMarkRow = 6
                Else
                    curSheetObj.Cells(j, curMarkRow) = "●"
                End If
            End If
        End If
    Next
End Function

Function dealversionupdate(sheetName As String, keyWord As String, strWBS As String)
    Set curSheetObj = Worksheets(sheetName)
    curSheetObj.Select
    If Not curSheetObj.Cells(1, 8) = "" Then
        curSheetObj.Columns("G:G").Select
        Selection.Delete Shift:=xlToLeft
    End If
   
    projectListCount = curSheetObj.Range("B65536").End(xlUp).Row
    curSheetObj.Range("G1:G2").Select
    Selection.Copy
    curSheetObj.Cells(1, 8).Select
    ActiveSheet.Paste
                
    For j = 3 To projectListCount
        If curSheetObj.Cells(j, 6) = "Diff" And InStr(curSheetObj.Cells(j, 4), keyWord) Then
            curSheetObj.Cells(j, 7) = "●"
            curSheetObj.Cells(1, 7) = strWBS
            GoTo dealEND
        End If
    Next
dealEND:

End Function

Private Sub GenWBS_Click()
    
    Application.DisplayAlerts = False
    
    Dim strWBSType As String
    strWBSType = MyTool.Cells(7, 16)
    Dim strWBS As String
    strWBS = MyTool.Cells(8, 16)
    
    For i = Sheets.Count To 1 Step -1
        If "表紙_集計" <> Sheets(i).Name And "Tool" <> Sheets(i).Name And "History" <> Sheets(i).Name Then
            'deal files with no comment like INF UNF KMP and so on start-------------------------------------------
            'INF or UNF
            If (InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 17)) > 0 And (MyTool.Cells(7, 17) = "●")) Or (InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 18)) > 0 And (MyTool.Cells(7, 18) = "●")) Then
                
                Call dealFileWithNoComment(Sheets(i).Name, "DriverVer", strWBS, strWBSType)
            'KMP
            ElseIf (InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 20)) > 0 And (MyTool.Cells(7, 20) = "●")) Then
                
                Call dealFileWithNoComment(Sheets(i).Name, "version", strWBS, strWBSType)
            'Version.ini
            ElseIf (InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 23)) > 0 And (MyTool.Cells(7, 23) = "●")) Then
                
                Call dealFileWithNoComment(Sheets(i).Name, "Ver_driver", strWBS, strWBSType)
            'SUB, GPD, PPD, Localize
            ElseIf (InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 19)) > 0 And (MyTool.Cells(7, 19) = "●")) Or (InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 21)) > 0 And (MyTool.Cells(7, 21) = "●")) _
            Or (InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 22)) > 0 And (MyTool.Cells(7, 22) = "●")) Or (InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 24)) > 0 And (MyTool.Cells(7, 24) = "●")) Then
                
                Call dealFileWithNoComment(Sheets(i).Name, "-keynes-", strWBS, strWBSType)
            'deal files with no comment like INF UNF KMP and so on end-------------------------------------------
            
            'deal file with comment like basic.ini and so on start***************************************************
            ElseIf ((strWBSType = "WBS案件対応") Or (strWBSType = "製品名対応") Or (strWBSType = "ファイル名対応") Or (strWBSType = "Generic対応")) _
            And (Not (InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 17)) > 0 Or InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 18)) > 0 _
            Or InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 19)) > 0 Or InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 20)) > 0 Or InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 21)) > 0 _
            Or InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 22)) > 0 Or InStr(UCase(Sheets(i).Name), MyTool.Cells(6, 23)) > 0)) Then
            
                Call dealFileWithComment(Sheets(i).Name, strWBS, strWBSType)
            'deal file with comment like basic.ini and so on end***************************************************
            ElseIf strWBSType = "禁則対応" And InStr(UCase(Sheets(i).Name), "CST_INI") Then
                Set conflictWBSDict = CreateObject("scripting.dictionary")
                conflictWBSNoStartRow = 9
                conflictWBSNoStartCol = 17
                conflictWBSNoCount = 1
                While True
                    If MyTool.Cells(conflictWBSNoStartRow, conflictWBSNoStartCol) = "" Or MyTool.Cells(conflictWBSNoStartRow, conflictWBSNoStartCol) = "END" Then
                        GoTo getConflictWBSNoEnd
                    Else
                        conflictWBSDict(conflictWBSNoCount) = MyTool.Cells(conflictWBSNoStartRow, conflictWBSNoStartCol).Value
                        conflictWBSNoCount = conflictWBSNoCount + 1
                        conflictWBSNoStartCol = conflictWBSNoStartCol + 1
                    End If
                Wend
getConflictWBSNoEnd:
                Call dealConflict(Sheets(i).Name)
            Else
            End If
            
            'deal speicial situation
            If InStr(UCase(Sheets(i).Name), "BASIC_INI") > 0 And (strWBSType = "Version更新") Then
                Call dealversionupdate(Sheets(i).Name, "Ver_Basic", strWBS)
            End If
            If InStr(UCase(Sheets(i).Name), "COMMAND_INI") > 0 And (strWBSType = "Version更新") Then
                Call dealversionupdate(Sheets(i).Name, "Ver_Command", strWBS)
            End If
            If InStr(UCase(Sheets(i).Name), "CST_INI") > 0 And (strWBSType = "Version更新") Then
                Call dealversionupdate(Sheets(i).Name, "Ver_Cst", strWBS)
            End If
            If InStr(UCase(Sheets(i).Name), "UISETUP_INI") > 0 And (strWBSType = "Version更新") Then
                Call dealversionupdate(Sheets(i).Name, "Ver_UISetup", strWBS)
            End If
            ThisWorkbook.Sheets(Sheets(i).Name).Select
            ThisWorkbook.Sheets(Sheets(i).Name).Range("A1").Select
        End If
    Next
    Application.DisplayAlerts = True
    'MsgBox ("Finish!")
    
End Sub

Private Sub CopyToCodeReviewBook_Click()

    Dim WBSNo As String
    Dim lineNumber As Integer 'for 表紙_集計
    
    lineNumber = 55
    fileCount = 1
    
    WBSNo = MyTool.Cells(8, 16)
    WBSNoBookName = MyTool.Cells(10, 18).Text
    WBSNOLastSheetName = "表紙_集計"
    
    For i = ThisWorkbook.Sheets.Count To 1 Step -1
        If "表紙_集計" <> ThisWorkbook.Sheets(i).Name And "Tool" <> ThisWorkbook.Sheets(i).Name And "History" <> ThisWorkbook.Sheets(i).Name Then
            
            If MyTool.Cells(7, 16) <> "禁則対応" Then
                If ThisWorkbook.Sheets(ThisWorkbook.Sheets(i).Name).Cells(1, 7).Text = WBSNo Then
                    ThisWorkbook.Activate
                    ThisWorkbook.Sheets(ThisWorkbook.Sheets(i).Name).Select
                    ThisWorkbook.Sheets(ThisWorkbook.Sheets(i).Name).Copy After:=Application.Workbooks(WBSNoBookName).Sheets("表紙_集計")
                    Workbooks(WBSNoBookName).Sheets("表紙_集計").Select
                    Workbooks(WBSNoBookName).Sheets("表紙_集計").Rows("55:56").Select
                    Selection.Copy
                    Workbooks(WBSNoBookName).Sheets("表紙_集計").Rows(CStr(lineNumber) + ":" + CStr(lineNumber + 1)).Select
                    ActiveSheet.Paste
                    Workbooks(WBSNoBookName).Sheets("表紙_集計").Cells(lineNumber, 6) = ThisWorkbook.Sheets(i).Name
                    Workbooks(WBSNoBookName).Sheets("表紙_集計").Cells(lineNumber + 1, 25) = "=" + ThisWorkbook.Sheets(i).Name + "!" + "R[" + CStr(2 - (lineNumber + 1)) + "]C[" + CStr(7 - 25) + "]"  'ThisWorkbook.Sheets(ThisWorkbook.Sheets(i).Name).Cells(2, 7).Text
                    tmpStr = "L" + CStr(lineNumber + 1) + ":R" + CStr(lineNumber + 1)
                    Workbooks(WBSNoBookName).Sheets("表紙_集計").Range(tmpStr).Select
                    ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:="", SubAddress:= _
                        ThisWorkbook.Sheets(i).Name + "!A1", TextToDisplay:=ThisWorkbook.Sheets(i).Name
                    Workbooks(WBSNoBookName).Sheets("表紙_集計").Cells(lineNumber + 1, 1) = fileCount
                    Workbooks(WBSNoBookName).Sheets("表紙_集計").Cells(lineNumber + 1, 1).Select
                    Selection.Font.ColorIndex = 2
                    fileCount = fileCount + 1
                    lineNumber = lineNumber + 2
                    GoTo nextWBS
                End If
            ElseIf InStr(UCase(ThisWorkbook.Sheets(i).Name), "CST_INI") Then
                ThisWorkbook.Activate
                ThisWorkbook.Sheets(ThisWorkbook.Sheets(i).Name).Select
                ThisWorkbook.Sheets(ThisWorkbook.Sheets(i).Name).Copy After:=Application.Workbooks(WBSNoBookName).Sheets("表紙_集計")
                Workbooks(WBSNoBookName).Sheets("表紙_集計").Select
                Workbooks(WBSNoBookName).Sheets("表紙_集計").Rows("55:56").Select
                Selection.Copy
                Workbooks(WBSNoBookName).Sheets("表紙_集計").Rows(CStr(lineNumber) + ":" + CStr(lineNumber + 1)).Select
                ActiveSheet.Paste
                Workbooks(WBSNoBookName).Sheets("表紙_集計").Cells(lineNumber, 6) = ThisWorkbook.Sheets(i).Name
                Workbooks(WBSNoBookName).Sheets("表紙_集計").Cells(lineNumber + 1, 25) = "=" + ThisWorkbook.Sheets(i).Name + "!" + "R[" + CStr(2 - (lineNumber + 1)) + "]C[" + CStr(7 - 25) + "]"  'ThisWorkbook.Sheets(ThisWorkbook.Sheets(i).Name).Cells(2, 7).Text
                tmpStr = "L" + CStr(lineNumber + 1) + ":R" + CStr(lineNumber + 1)
                Workbooks(WBSNoBookName).Sheets("表紙_集計").Range(tmpStr).Select
                ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:="", SubAddress:= _
                    ThisWorkbook.Sheets(i).Name + "!A1", TextToDisplay:=ThisWorkbook.Sheets(i).Name
                lineNumber = lineNumber + 2
            End If

        End If
nextWBS:
    Next i

End Sub


Private Sub Tool_Click()
    Application.CutCopyMode = False
    'clearSheetContent "表紙_集計"
    Application.DefaultFilePath = ActiveWorkbook.Path
    lstHtmlFileName = "Tool"
    getHtmlFiles
End Sub

Function getHtmlFiles()
    Dim filetoopen As Variant
    Dim i As Integer

    filetoopen = Application.GetOpenFilename("HTML Files (*.htm; *.html), *.htm;*.html", Title:="Choose files", MultiSelect:=True)
    If Not IsArray(filetoopen) Then
        
    Else
        For i = LBound(filetoopen) To UBound(filetoopen)
            convertHtmlToExcel CStr(filetoopen(i))
            fileCount = fileCount + 1
            fileInformationRecord
        Next
    End If
End Function

Function convertHtmlToExcel(htmlPath As String)
    readHtmlName htmlPath
    createNewSheet
    readHtml htmlPath
    dealFileContent
    adjustFileFormat
    showDiffOnly
End Function

Function readHtmlName(htmlPath As String)
    'read htnl name
    Dim fso As Object
    Set fso = CreateObject("Scripting.FileSystemObject")
    curHtmlFileName = fso.GetBaseName(htmlPath) 'GetFileName
    curSheetName = curHtmlFileName
End Function


'read the html result
Function readHtml(htmlPath As String)
    Application.DisplayAlerts = False
    Set htmObj = Workbooks.Open(htmlPath)
    Application.DisplayAlerts = True
    'htmObj.Worksheets(curHtmlFileName).Range("A1:IV65535").Select
    projectListCount = htmObj.Worksheets(curSheetName).Range("B65536").End(xlUp).Row
    projectListCount2 = htmObj.Worksheets(curSheetName).Range("D65536").End(xlUp).Row
    If projectListCount < projectListCount2 Then
        projectListCount = projectListCount2
    End If
    'Worksheets(curSheetName).Range(Selection, Selection.End(xlDown)).Select
    cellPos = "D" & CStr(projectListCount)
    htmObj.Worksheets(curSheetName).Range("A1:" & cellPos).Select
    Application.DisplayAlerts = False
    Selection.Copy
    ThisWorkbook.Sheets(curHtmlFileName).Activate
    ThisWorkbook.Sheets(curHtmlFileName).Range("A1").Select
    ActiveSheet.Paste
    'htmObj.Worksheets(curHtmlFileName).Cells.Select
    'Sheets(curHtmlFileName).Select
    'Sheets(curHtmlFileName).Copy after:=ThisWorkbook.Sheets(lstHtmlFileName)
    htmObj.Close False
    Application.DisplayAlerts = True
    
    
    'second method
'    Set h = CreateObject("Microsoft.XMLHTTP")
'    h.Open "get", htmlPath, False
'    h.send
'    'yuan = convertHtmlToString(h.responsebody)
'    yuan = h.responsetext
'
'    Dim MyData As New DataObject
'    MyData.SetText yuan
'    MyData.PutInClipboard
'    'Paste html information to excel
'    Worksheets(curSheetName).Range("A3").Select
'    ActiveSheet.Paste
    
    'old solution
'    'read html content
'    Set iex = CreateObject("internetexplorer.application")
'    iex.Visible = False
'    iex.navigate htmlPath
'    'make sure the status is complete
'    While iex.readystate <> 4
'    Wend
'    'copy html information to clipboard
'    Dim MyData As New DataObject
'    MyData.SetText iex.document.body.innerhtml 'innertext, innerhtml, outerhtml
'    MyData.PutInClipboard
'    'Paste html information to excel
'    Worksheets(curSheetName).Range("A3").Select
'    ActiveSheet.Paste
End Function


'deal file Content
Function dealFileContent()
    Worksheets(curSheetName).Rows("1:1").Select
    Selection.Insert Shift:=xlDown
    Worksheets(curSheetName).Range("B1") = curHtmlFileName
    
    Worksheets(curSheetName).Range("F1") = "Diff"
    Worksheets(curSheetName).Range("F2").Select
    ActiveCell.FormulaR1C1 = "=COUNTIF(R[1]C:R[65534]C,""Diff"")"
    Worksheets(curSheetName).Range("F3").Select
    ActiveCell.FormulaR1C1 = "=IF(RC[-4]<>RC[-2],""Diff"","""")"
    Worksheets(curSheetName).Range("F3").Select
    Selection.Copy
    projectListCount = Worksheets(curSheetName).Range("B65536").End(xlUp).Row
    'Worksheets(curSheetName).Range(Selection, Selection.End(xlDown)).Select
    cellPos = "F" & CStr(projectListCount)
    Worksheets(curSheetName).Range("F4:" & cellPos).Select
    ActiveSheet.Paste
    ActiveWindow.SmallScroll Down:=-6
    Selection.Font.ColorIndex = 3
    Selection.Font.Bold = True
    
    Worksheets(curSheetName).Range("G1") = "WBS"
    Worksheets(curSheetName).Range("G2").Select
    ActiveCell.FormulaR1C1 = "=COUNTIF(R[1]C:R[65533]C,""●"")"
    

End Function

'adjust file format
Function adjustFileFormat()
    Worksheets(curSheetName).Cells(1, 1).ColumnWidth = 3
    Worksheets(curSheetName).Cells(1, 2).ColumnWidth = 75
    Worksheets(curSheetName).Cells(1, 3).ColumnWidth = 3
    Worksheets(curSheetName).Cells(1, 4).ColumnWidth = 75
    Worksheets(curSheetName).Cells(1, 5).ColumnWidth = 3
    Worksheets(curSheetName).Range("F1:P1").ColumnWidth = 5
    
    Worksheets(curSheetName).Range("B1").Select
    Selection.Font.Bold = True
    Selection.Font.ColorIndex = 5
    Selection.Font.Size = 24
    
    Worksheets(curSheetName).Range("B1:P1").Select
    Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone
    Selection.Borders(xlEdgeLeft).LineStyle = xlNone
    Selection.Borders(xlEdgeTop).LineStyle = xlNone
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
        .ColorIndex = 5
    End With
    Selection.Borders(xlEdgeRight).LineStyle = xlNone
    Selection.Borders(xlInsideVertical).LineStyle = xlNone
    Application.CommandBars("Borders").Visible = False
    
    Worksheets(curSheetName).Range("B2,D2,F2").Select
    Worksheets(curSheetName).Range("F1:G1").Activate
    With Selection.Interior
        .ColorIndex = 5
        .Pattern = xlSolid
    End With
    Selection.Font.ColorIndex = 2
    Selection.Font.Bold = True
    
    Worksheets(curSheetName).Columns("A:A").Select
    Selection.Interior.ColorIndex = xlNone
    Worksheets(curSheetName).Columns("C:C").Select
    Selection.Interior.ColorIndex = xlNone
    
    'ActiveWindow.DisplayGridlines = False
    
    Worksheets(curSheetName).Range("F2").Select
    Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .Weight = xlMedium
        .ColorIndex = xlAutomatic
    End With
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .Weight = xlMedium
        .ColorIndex = xlAutomatic
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
        .ColorIndex = xlAutomatic
    End With
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlMedium
        .ColorIndex = xlAutomatic
    End With
    
    Worksheets(curSheetName).Range("G2").Select
    Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .Weight = xlMedium
        .ColorIndex = xlAutomatic
    End With
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .Weight = xlMedium
        .ColorIndex = xlAutomatic
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
        .ColorIndex = xlAutomatic
    End With
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlMedium
        .ColorIndex = xlAutomatic
    End With
    
    Worksheets(curSheetName).Range("F2:G2").Select
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlCenter
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Selection.Font.ColorIndex = 5
    Selection.Font.Bold = True
    
    Worksheets(curSheetName).Rows("3:3").Select
    ActiveWindow.FreezePanes = True
    ActiveWindow.SmallScroll Down:=0
    
    Worksheets(curSheetName).Cells.Select
    Worksheets(curSheetName).Cells.EntireRow.AutoFit
    Worksheets(curSheetName).Range("A1").Select
End Function

Function fileInformationRecord()
    Worksheets("表紙_集計").Select
    Worksheets("表紙_集計").Range("D1") = "code"
    Worksheets("表紙_集計").Range("E1") = "comment"
    Worksheets("表紙_集計").Cells(fileCount + 1, 2) = curSheetName
    Worksheets("表紙_集計").Cells(fileCount + 1, 2).Select
    ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:="", SubAddress:= _
        curSheetName + "!A1", TextToDisplay:=curSheetName
    Worksheets("表紙_集計").Cells(fileCount + 1, 3).Select
    ActiveCell.FormulaR1C1 = "=" + curSheetName + "!R[" + CStr(1 - fileCount) + "]C[3]"
    Worksheets("表紙_集計").Cells(fileCount + 1, 4).Select
    ActiveCell.FormulaR1C1 = "=COUNTIF(" + curSheetName + "!R[" + CStr(2 - fileCount) + "]C[3]:R[40000]C[20],""●"")"
    Worksheets("表紙_集計").Cells(fileCount + 1, 5).Select
    ActiveCell.FormulaR1C1 = "=COUNTIF(" + curSheetName + "!R[" + CStr(2 - fileCount) + "]C[2]:R[40000]C[20],""※"")"
End Function

Function clearSheetContent(sheetName As String)
    Worksheets(sheetName).Select
    Worksheets(sheetName).Cells.Select
    Selection.Clear
    Worksheets(sheetName).Range("A1").Select
End Function

Function deleteAllReportSheets()
    Application.DisplayAlerts = False
    For i = Sheets.Count To 1 Step -1
        If "表紙_集計" <> Sheets(i).Name And "Tool" <> Sheets(i).Name And "History" <> Sheets(i).Name Then
            Sheets(i).Delete
        End If
    Next i
    Application.DisplayAlerts = True
End Function


'create a new sheet for code compare
Function createNewSheet()
    If isSheetExist(curHtmlFileName) Then
        'Sheets("Sheet2").Cells.ClearContents clear content only
        'Sheets("Sheet2").Cells.Clear clear content and style
        Sheets(curHtmlFileName).Cells.Clear
        Worksheets(curHtmlFileName).Select
    Else
        Worksheets.Add After:=Worksheets(lstHtmlFileName)
        ActiveSheet.Name = curHtmlFileName
        lstHtmlFileName = curHtmlFileName
    End If
    curSheetName = curHtmlFileName
End Function

Function showDiffOnly()
    Sheets(curHtmlFileName).Columns("F:F").Select
    Selection.AutoFilter
    'Selection.AutoFilter Field:=1, Criteria1:="Diff"
    Sheets(curHtmlFileName).Range("A1").Select
End Function

'convert Html file's content to String
'Function convertHtmlToString(content) As String
'    For i = 1 To LenB(content)
'    Text = AscB(MidB(content, i, 1))
'    If Text < &H80 Then
'    body = body & Chr(Text)
'    Else
'    file = AscB(MidB(content, i + 1, 1))
'    body = body & Chr(CLng(Text) * &H100 + CInt(file))
'    i = i + 1
'    End If
'    Next
'    convertHtmlToString = body
'End Function

Function isSheetExist(sheetName As String) As Boolean
    isSheetExist = False
    For i = 1 To Sheets.Count
        If sheetName = Sheets(i).Name Then
            isSheetExist = True
            Exit For
        End If
    Next i
End Function
