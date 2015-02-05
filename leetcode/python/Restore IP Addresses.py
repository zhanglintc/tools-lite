# Restore IP Addresses
# for leetcode problems
# 2015.02.05 by zhanglin

# Problem:
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        fina_lst = []
        self.helper(s, 0, "", fina_lst)
        return fina_lst

    def helper(self, s, times, IpAdd, fina_lst):
        if not s or times == 4:
            if not s and times == 4:
                fina_lst.append(IpAdd[1:])

            return

        for i in range(1, len(s) + 1):
            if 0 <= int(s[:i]) <= 255 and self.isValidIp(s[:i]):
                self.helper(s[i:], times + 1, IpAdd + "." + s[:i], fina_lst)

    def isValidIp(self, ip):
        if len(ip) > 1 and ip[0] == "0":
            return False

        return True


