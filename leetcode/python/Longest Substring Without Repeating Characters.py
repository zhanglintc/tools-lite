# Longest Substring Without Repeating Characters
# for leetcode problems
# 2014.09.08 by zhanglin

# Problem:
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc",
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        dikt = {}       # to store the position of each character last occurred
        beg_idx = -1    # beginning position of longest substring, initialized as -1
        fin_max = 0     # the answer to return

        for i in range(len(s)):
            if dikt.get(s[i]) > beg_idx:    # only this character's index bigger than beg_idx means this character has occurred before
                beg_idx = dikt[s[i]]        # update the longest sub-string's beginning position

            fin_max = max(fin_max, i - beg_idx) # update the longest substring value

            dikt[s[i]] = i # update the position of this character each time

        return fin_max


