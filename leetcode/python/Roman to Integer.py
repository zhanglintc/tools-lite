# Roman to Integer
# for leetcode problems
# 2014.09.21 by zhanglin

# Problem:
# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return an integer
    def romanToInt(self, s):
        convert_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        
        last = None # the previous result
        digit = 0 # the answer

        s = s[::-1] # reverse this string

        for i in s: # s has been reversed before, thus this mean traverse from the end of the string
            if convert_dict[i] < last: # if this number smaller than previous one, reduce it
                digit -= convert_dict[i]
            else: # otherwise add it to the answer
                digit += convert_dict[i]

            last = convert_dict[i] # store the previous one

        return digit # return answer


