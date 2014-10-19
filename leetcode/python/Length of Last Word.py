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
        space = ' '
        length = 0
        last_character = space

        for this_character in s:
            # not space
            if this_character != space:
                # space occurred before, reset the length
                if last_character == space:
                    length = 1

                # count length normally
                else:
                    length += 1

                # store this character
                last_character = this_character

            # space, jump over
            else:
                last_character = space
                continue

        return length


