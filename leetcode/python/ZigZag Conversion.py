# ZigZag Conversion
# for leetcode problems
# 2014.08.19 by zhanglin

# Problem:
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    # @return a string
    def convert(self, s, nRows):
        length = len(s) # get length

        if length == 0 or nRows <= 1: # special case
            return s

        new_str = "" # new a string
        row = 0 # up to down
        while row < length and row < nRows:
            # first line(line 0):
            index = row
            new_str += s[index]

            line = 1 # line 1 to line N
            while index < length:
                if row == 0 or row == nRows - 1: # first or last row
                    index += (nRows * 2 - 2)

                else: # other rows
                    if line & 0x01: # odd line
                        index += ((nRows - row - 1) * 2)
                    else: # even line
                        index += (row * 2)

                line += 1 # to next line

                if index < length: # if in the range
                    new_str += s[index]

            row += 1 # to next row

        return new_str


