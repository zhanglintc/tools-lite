# Length of Last Word
# for leetcode problems
# 2014.10.19 by zhanglin

# Problem:
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example, 
# Given s = "Hello World",
# return 5.

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        words = s.split()

        if words == []:
            return 0

        else:
            return len(words[-1])

s = Solution()
print s.lengthOfLastWord(' 1  ')


