# Count and Say
# for leetcode problems
# 2014.09.30 by zhanglin

# Problem:
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.

class Solution:
    # @return a string
    def countAndSay(self, n):
        count_and_said = '1'
        count_and_say  = ''

        if n == 0:
            return ''

        if n == 1:
            return '1'


        for no_matter_what_here in range(n - 1): # n - 1 times
            count_and_say = ''
            last_C = None

            for this_C in count_and_said:
                if this_C != last_C: # append times of last character only if a new character appears
                    if last_C != None: # append only if last character not None
                        count_and_say += (str(times) + last_C)
                    last_C = this_C # store this character
                    times = 1 # reset times
                else: # else count times
                    times += 1

            # reach the end, append remaining data
            count_and_say += (str(times) + last_C)
            count_and_said = count_and_say

        return count_and_say


