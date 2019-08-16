VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Sheet1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Dim datumGivenRow
Dim datumGivenLine
Dim datumCalcRow
Dim datumCalcLine
Dim lineOffsetMax
Dim rowOffsetMax

Dim givenArea As New Collection
Dim calcArea As New Collection

' Fullfill global area varibals
Sub MakeWorkArea(ByRef givenArea, ByRef calcArea As Collection)
    ' Cleanup before use
    While givenArea.Count > 0
        givenArea.Remove 1
    Wend
    While calcArea.Count > 0
        calcArea.Remove 1
    Wend

    ' Do make
    For lineOffset = 0 To lineOffsetMax
        givenLine = datumGivenLine + lineOffset
        calcLine = datumCalcLine + lineOffset
        For rowOffset = 0 To rowOffsetMax
            givenRow = datumGivenRow + rowOffset
            calcRow = datumCalcRow + rowOffset

            givenCL = Array(givenRow, givenLine)
            calcCL = Array(calcRow, calcLine)
            givenArea.Add (givenCL)
            calcArea.Add (calcCL)
        Next rowOffset
    Next lineOffset
End Sub

' Copy data and set color
Sub CopyOriginalData()
    For i = 1 To givenArea.Count
        fromRow = givenArea.Item(i)(0)
        fromLine = givenArea.Item(i)(1)
        toRow = calcArea.Item(i)(0)
        toLine = calcArea.Item(i)(1)

        Cells(toRow, toLine) = Cells(fromRow, fromLine)
        If Not IsEmpty(Cells(toRow, toLine)) Then
            Cells(toRow, toLine).Interior.ColorIndex = 8
        Else
            Cells(toRow, toLine).Interior.ColorIndex = 4
        End If
    Next i
End Sub

' Forcast by existing data
Sub ForcastBwteenWeeks()
    For i = 1 To givenArea.Count
        fromRow = givenArea.Item(i)(0)
        fromLine = givenArea.Item(i)(1)
        toRow = calcArea.Item(i)(0)
        toLine = calcArea.Item(i)(1)

        If IsEmpty(Cells(fromRow, fromLine)) Then
            theHour = Int(i - 1) Mod 13 + datumGivenRow
            theDay = Int((i - 1) / 13) Mod 7 + datumGivenLine

            the1stWeek = Cells(theHour, theDay + 7 * 0)
            the2ndWeek = Cells(theHour, theDay + 7 * 1)
            the3rdWeek = Cells(theHour, theDay + 7 * 2)
            the4thWeek = Cells(theHour, theDay + 7 * 3)

            weeks = Array(the1stWeek, the2ndWeek, the3rdWeek, the4thWeek)
            cnt = 0
            For wk = 0 To UBound(weeks)
                If Not IsEmpty(weeks(wk)) Then
                    cnt = cnt + 1
                End If
            Next wk
            If cnt Then
                avg = WorksheetFunction.Sum(weeks) / cnt
                Cells(toRow, toLine) = avg
            End If
        Else
            ' Debug.Print "skipped cause not empty"
        End If
    Next i
End Sub

Sub ForcastEachDay()
    ' Each day
    For theDay = 1 To calcArea.Count Step 13
        valCnt = 0
        daySum = 0

        For hourOffset = 0 To 12
            cl = calcArea.Item(theDay + hourOffset)
            theRow = cl(0)
            theLine = cl(1)

            theVal = Cells(theRow, theLine).Value
            If Not IsEmpty(theVal) Then
                valCnt = valCnt + 1
                daySum = daySum + theVal
            End If
        Next hourOffset

        ' Data exist for this day, calculate average for within this day
        If valCnt Then
            avg = daySum / valCnt

            For hourOffset = 0 To 12
                cl = calcArea.Item(theDay + hourOffset)
                theRow = cl(0)
                theLine = cl(1)
                If IsEmpty(Cells(theRow, theLine)) Then
                    Cells(theRow, theLine) = avg
                End If
            Next hourOffset
        End If
    Next theDay
End Sub

Sub ForcastWithinWeek()
    For theDay = 1 To calcArea.Count Step 13
        valCnt = 0
        daySum = 0

        For hourOffset = 0 To 12
            cl = calcArea.Item(theDay + hourOffset)
            theRow = cl(0)
            theLine = cl(1)

            theVal = Cells(theRow, theLine).Value
            If Not IsEmpty(theVal) Then
                valCnt = valCnt + 1
                daySum = daySum + theVal
            End If
        Next hourOffset

        ' Data not exist for this day, calculate average within this week
        If valCnt = 0 Then
            For hourOffset = 0 To 12
                sn = theDay + hourOffset
                cl = calcArea.Item(theDay + hourOffset)
                theRow = cl(0)
                theLine = cl(1)

                curWeekBase = (Int((sn - 1) / (7 * 13))) * 7
                thisMonday = Cells(theRow, datumCalcLine + curWeekBase + 0)
                thisTuesday = Cells(theRow, datumCalcLine + curWeekBase + 1)
                thisWednesday = Cells(theRow, datumCalcLine + curWeekBase + 2)
                thisThursday = Cells(theRow, datumCalcLine + curWeekBase + 3)
                thisFriday = Cells(theRow, datumCalcLine + curWeekBase + 4)
                thisSaturday = Cells(theRow, datumCalcLine + curWeekBase + 5)
                thisSunday = Cells(theRow, datumCalcLine + curWeekBase + 6)

                thisWeek = Array(thisMonday, thisTuesday, thisWednesday, thisThursday, thisFriday, thisSaturday, thisSunday)
                cnt = 0
                all = 0
                For d = 0 To UBound(thisWeek)
                    If Not IsEmpty(thisWeek(d)) Then
                        cnt = cnt + 1
                    End If
                Next d
                If cnt Then
                    avg = WorksheetFunction.Sum(thisWeek) / cnt
                    Cells(theRow, theLine) = avg
                End If
            Next hourOffset
        End If
    Next theDay
End Sub

' Entry
Sub Main()
    ' Initialize global variables
    datumGivenRow = 5
    datumGivenLine = 3
    datumCalcRow = 21
    datumCalcLine = 3
    lineOffsetMax = 28 - 1
    rowOffsetMax = 13 - 1
    Call MakeWorkArea(givenArea, calcArea)

    ' Begin work
    CopyOriginalData
    ForcastBwteenWeeks
    ForcastEachDay
    ForcastWithinWeek
End Sub
