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
            while k > 0 and needle[k] != needle[q]:
                k = Pi[k - 1]
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
        for i in range(0, n):
            while q > 0 and needle[q] != haystack[i]:
                q = Pi[q - 1]
            if needle[q] == haystack[i]:
                q = q + 1
            if q == m:
                return haystack[i - m + 1:]
        return None


