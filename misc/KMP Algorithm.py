class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    # @KMP algorithms
    def ComputePrefixFunction(self, needle): # caculate Partial Match Table (PMT)
        Pi = [0 for i in range(len(needle))]
        m = len(needle)
        Pi[0] = 0
        k = 0
        for q in range(1, m):
            if k > 0 and needle[k] != needle[q]:
                k = 0
            if needle[k] == needle[q]:
                k = k + 1
            Pi[q] = k
        return Pi
    
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return haystack
        Pi = self.ComputePrefixFunction(needle)
        q = 0 # index of needle, it also means the number of characters has already matched
        i = 0 # index of haystack
        saved_hay = 0 # cache of haystack index
        while i < n:
            if needle[q] == haystack[i]: # if matched
                q += 1
                i += 1
            else: # if not matched
                i = saved_hay # reset i
                if q == 0: # if no character matched before, one step move forward
                    i += 1
                else: # move_step = already_matched - PMT[already_matched - 1]
                    i += (q - Pi[q - 1])
                q = 0 # reset q
                saved_hay = i # update saved_hay
            if q == m: # if q meets the end, return True
                return haystack[i - m:]
        return None


