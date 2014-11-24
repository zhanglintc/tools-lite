# 3Sum Closest
# for leetcode problems
# 2014.11.20 by zhanglin

# Problem:
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# For example, given array S = {-1 2 1 -4}, and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        length = len(num)
        min_bias = None

        num.sort()

        for i in range(1, length - 1):
            left = 0
            right = length - 1

            while left < right:
                this_sum = num[left] + num[i] + num[right]
                bias = abs(this_sum - target)

                if bias < min_bias or min_bias == None:
                    min_bias = bias
                    threesum = this_sum

                if threesum == target:
                        return threesum

                elif threesum < target:
                    left += 1

                else:
                    right -= 1


        return threesum


s = Solution()
print s.threeSumClosest([1,1,-1,-1,3], 3)

