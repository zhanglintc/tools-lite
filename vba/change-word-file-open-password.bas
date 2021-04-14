Sub UnProtectAllDocFiles()
    On Error Resume Next
    Const strRootPath = "folder_path"
    Const strOldPassword = "old_password"
    Const strNewPassword = "new_password"
    Dim oDoc As Document
    Dim fso, oFolder, oFile
    Set fso = CreateObject("Scripting.FileSystemObject")
    Set oFolder = fso.GetFolder(strRootPath)
    For Each oFile In oFolder.Files
        Set oDoc = Documents.Open(FileName:=oFile.Path, PasswordDocument:=strOldPassword)
        oDoc.Saved = False
        oDoc.SaveAs FileName:=oFile.Path, Password:=strNewPassword, WritePassword:=""
        oDoc.Close
    Next
    MsgBox "done"
End Sub
