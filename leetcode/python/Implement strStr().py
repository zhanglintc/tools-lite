# Implement strStr()
# for leetcode problems
# 2014.10.20 by zhanglin

# Problem:
# Implement strStr().

# Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        saved_hay = 0
        cur_hay   = 0
        cur_ndl   = 0

        # while no one meets the end
        while cur_hay < len(haystack) and cur_ndl < len(needle):
            # if not matched, reset cur_ndl but saved_hay cur_hay move forward
            if haystack[cur_hay] != needle[cur_ndl]:
                saved_hay += 1

                cur_hay = saved_hay
                cur_ndl = 0

            # if matched, both cur_hay and cur_ndl move forward
            else:
                cur_hay += 1
                cur_ndl += 1

        # if cur_ndl meets the end, means needle in the haystack
        if cur_ndl == len(needle):
            return haystack[saved_hay:]

        # else needle not in the haystack
        else:
            return None


