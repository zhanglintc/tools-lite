#include <Array.au3>
#Include <File.au3>

global $FileNumber = 0 ; 记录数组维数，全局变量
global $FileArray[1] ; 返回的文件名主数组（全路径），全局变量
global $result = "result.txt"

FindFiles("E:\Subv_Work\DI_9.4.0.0\IT5_Icarus_v3.1\KMSrc_2.06.45_7.0.1.0", "*") ; 这里改为你自己要遍历的文件夹
; $FileArray[0] = $FileNumber
; _ArrayDisplay($FileArray, "Pictures");调用“Array.au3”的子函数函数，显示整个数组信息
for $i = 1 to $FileNumber
    FileWriteLine($result, $FileArray[$i])
next

func FindFiles($path, $filelx)
    local $filelist
    local $folders
    local $i, $j, $newpath
    $filelist = _FileListToArray ($path, $filelx, 1)

    if not @error then
        if $filelist[0] > 0 then
            for $i = 1 to $filelist[0]
                ConsoleWrite ($path & "\" & $filelist[$i] & @CRLF)
                ; $FileNumber = $FileNumber + 1
                ; redim $FileArray[UBound($FileArray) + 1]
                ; $FileArray[$FileNumber] = $path & "\" & $filelist[$i]
            next
        endif
    endif

    $folders = _FileListToArray ($path, "*", 2)
    if not @error then
        if $folders[0] > 0 then
            for $j = 1 to $folders[0]
                $newpath = $path & "\" & $folders[$j]
                FindFiles($newpath, $filelx)
            next
        endif
    endif
endfunc