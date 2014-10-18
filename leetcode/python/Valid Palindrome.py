# Valid Palindrome
# for leetcode problems
# 2014.10.19 by zhanglin

# Problem:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'

        left_to_right = 0
        right_to_left = len(s) - 1

        while left_to_right < len(s):
            if s[left_to_right].lower() not in alphanumeric:
                left_to_right += 1
                continue

            if s[right_to_left].lower() not in alphanumeric:
                right_to_left -= 1
                continue

            if s[left_to_right].lower() != s[right_to_left].lower():
                return False

            left_to_right += 1
            right_to_left -= 1

        return True

s = Solution()
print s.isPalindrome('a:/ab')


