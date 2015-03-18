# Reverse Bits
# for leetcode problems
# 2015.03.18 by zhanglin

# Problem:
# Reverse bits of a given 32 bits unsigned integer.

# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).

# Follow up:
# If this function is called many times, how would you optimize it?

# Related problem: Reverse Integer

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution: 
    # @param n, an integer 
    # @return an integer 
    def reverseBits(self, n): 
        ans = 0 
        for i in range(0,32): 
            #get information 
            x = 1 & n 
            # shift the input num by 1 
            n >>= 1 
            # set the leftmost bit in input num to 0 becuase python shift is arithmetic 
            n &= 0x7fffffff 
            #move the x to correct location 
            x <<= (31- i) 
            # set the bit in the answer 
            ans |= x 
        return ans


