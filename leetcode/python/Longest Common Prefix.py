# Longest Common Prefix
# for leetcode problems
# 2014.09.08 by zhanglin

# Problem:
# Write a function to find the longest common prefix string amongst an array of strings.
# Don's know what longest common prefix is? See http://en.wikipedia.org/wiki/LCP_array

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        ret_str = ''

        if strs == []:
            return ret_str

        short = strs[0] # find the shortest string to save time
        for s in strs:
            if s < short:
                short = s

        for i in range(len(short)): # traverse the shortest string
            add = True
            for s in strs: # traverse the whole strs
                if short[i] == s[i]: # find this char, jump over
                    continue
                else: # doesn't find this char, set the flag as false, and break
                    add = False
                    break

            if add == False: # if the flag is false, break
                break

            ret_str += s[i] # if everthing is OK, add this char to the end of ret_str

        return ret_str


