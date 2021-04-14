Sub UnProtectAllDocFiles()
    On Error Resume Next
    Const strRootPath = "folder_path"
    Dim fso, oFolder
    Set fso = CreateObject("Scripting.FileSystemObject")
    fso.Application.Options.WarnBeforeSavingPrintingSendingMarkup = False
    Set oFolder = fso.GetFolder(strRootPath)
    UnProtectDocFilesUnderFolder oFolder
    MsgBox "done"
End Sub

Sub UnProtectDocFilesUnderFolder(oFolder)
    On Error Resume Next
    Dim oSubFolder, oFile
    Dim oDoc As Document
    Const strPassword = "old_password"
    Const newPassword = "new_password"

    For Each oSubFolder In oFolder.SubFolders
        UnProtectDocFilesUnderFolder oSubFolder
        For Each oFile In oSubFolder.Files
            Set oDoc = Documents.Open(FileName:=oFile.Path)
            oDoc.Options.WarnBeforeSavingPrintingSendingMarkup = False
            oDoc.Unprotect Password:=strPassword
            oDoc.Protect Password:=newPassword, NoReset:=False, Type:= _
            wdAllowOnlyReading, UseIRM:=False, EnforceStyleLock:=False
            oDoc.Save
            oDoc.Close
        Next
    Next
End Sub
