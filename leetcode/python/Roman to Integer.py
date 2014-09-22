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

        s.reverse()
        last = 'I'
        digit = 0
        for i in s:
            if convert_dict[i] < convert_dict[last]:
                digit -= convert_dict[i]
            else:
                digit += convert_dict[i]

            last = i

        return digit

s = Solution()
print(s.romanToInt("X"))


