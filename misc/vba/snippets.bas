Sub addCircle()
    For curSheet = 2 To Sheets.Count Step 1
        rowEnd = Sheets(curSheet).Range("D65536").End(xlUp).Row
        For curRow = 3 To rowEnd Step 1
            If InStr(Sheets(curSheet).Cells(curRow, 6), "Diff") >= 1 And InStr(Sheets(curSheet).Cells(curRow, 4), "KOAY") >= 1 Then
                Sheets(curSheet).Cells(curRow, 7) = "œ"
            End If
        Next curRow
    Next curSheet
End Sub
