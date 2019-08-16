Sub addCircle()
    For curSheet = 3 To Sheets.Count Step 1
        rowEnd = Sheets(curSheet).Range("D65536").End(xlUp).Row
        Sheets(curSheet).Cells(1, 7) = "WBS_No_XXX"
        For curRow = 3 To rowEnd Step 1
            If InStr(Sheets(curSheet).Cells(curRow, 6), "Diff") >= 1 Then
                Sheets(curSheet).Cells(curRow, 7) = "●"
            End If
        Next curRow
    Next curSheet
End Sub

'refer to: http://stackoverflow.com/questions/22498393/is-it-possible-to-return-error-code-to-vba-from-batch-file
Sub getExitCode()
    Set oSHELL = VBA.CreateObject("WScript.Shell")
    'what does "0", "True" mean below?
    exitCode = oSHELL.Run(ThisWorkbook.Path & "\exit250.exe", 0, True)
    Debug.Print exitCode
End Sub

Sub addLinks()
    Sheets("表紙_集計").Select

    Row = 62
    For Page = Sheets.Count To 2 Step -1
        pageName = Sheets(Page).Name

        Range(Cells(Row, 12), Cells(Row, 20)).Select
        ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:="", SubAddress:=pageName & "!A1", TextToDisplay:=pageName

        Row = Row + 2
    Next Page
End Sub

