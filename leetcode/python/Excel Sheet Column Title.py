# Excel Sheet Column Title
# for leetcode problems
# 2014.12.26 by zhanglin

# Problem:
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB

# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.

class Solution:
    # @return a string
    def convertToTitle(self, num):
        ConvStr = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        ExcelStr = ""
        NumList = []
        isMultiple = True if num % 26 == 0 else False

        i = 1
        while 26 ** i < num:
            NumList.append(26 ** i)
            i += 1

        NumList.reverse()

        for i in NumList:
            ExcelStr += ConvStr[num / i - (1 if isMultiple else 0)]
            num %= i

        return ExcelStr + ConvStr[num % 26]

s = Solution()
print s.convertToTitle(701)


