class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    # @KMP algorithms
    def ComputePrefixFunction(self, needle):
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
        q = 0
        i = 0
        saved_hay = 0
        while i < n:
            if needle[q] == haystack[i]:
                q += 1
                i += 1
            else:
                i = saved_hay
                if q == 0:
                    i += 1
                else:
                    i += (q - Pi[q - 1])
                q = 0
                saved_hay = i
            if q == m:
                return haystack[i - m:]
        return None


