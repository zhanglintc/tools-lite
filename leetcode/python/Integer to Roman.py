# Integer to Roman
# for leetcode problems
# 2014.09.21 by zhanglin

# Problem:
# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return a string
    def intToRoman(self, num):
        '''
        units    = ['I','II','III','IV','V','VI','VII','VIII','IX']
        tens     = ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        hundreds = ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        kilobis  = ['M','MM','MMM']
        '''
        convert_list = [
            ['I','II','III','IV','V','VI','VII','VIII','IX'],
            ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
            ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
            ['M','MM','MMM']
        ]

        lst = []
        while num:
            lst.append(num % 10)
            num //= 10
            print lst

        roman = ''
        while lst:
            roman += convert_list[len(lst) - 1][lst.pop() - 1]

        return roman

s = Solution()
print s.intToRoman(3999)
