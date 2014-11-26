# Letter Combinations of a Phone Number
# for leetcode problems
# 2014.11.25 by zhanglin

# Problem:
# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.

# Image see: https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
# Or the sketch by zhanglin:
# ----------------------- #
#  1       2       3      #
# ($_$)   (abc)   (def)   #
#                         #
#  4       5       6      #
# (ghi)   (jkl)   (mno)   #
#                         #
#  7       8       9      #
# (pqrs)  (tuv)   (wxyz)  #
# ----------------------- #

# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        fina_lst = []

        self.helper(digits, '', fina_lst)

        return fina_lst

    def helper(self, digits, this_str, fina_lst):
        conv_map = {
            '1': ''    , '2': 'abc', '3': 'def' ,
            '4': 'ghi' , '5': 'jkl', '6': 'mno' ,
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
            '0': '',
        }

        # if all digit in digits is used, append the combination to the fina_lst
        if not digits:
            fina_lst.append(this_str)
            return

        # while digits[0] is invalid(means relevant to no characters), remove it
        while not conv_map[digits[0]]:
            digits = digits[1:]

        # recursive
        for ch in conv_map[digits[0]]:
            self.helper(digits[1:], this_str + ch, fina_lst)


