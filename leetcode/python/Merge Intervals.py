# Merge Intervals
# for leetcode problems
# 2015.03.20 by zhanglin

# Problem:
# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def interval_cmp(self, p, q):
        if p.start < q.start:
            return -1

        elif p.start > q.start:
            return 1

        else:
            if p.end < q.end:
                return -1

            elif p.end > q.end:
                return 1

            else:
                return 0

    def merge(self, intervals):
        intervals = sorted(intervals, cmp = self.interval_cmp)

        new_intervals = []
        this_interval = None

        for i in range(len(intervals)):
            if not this_interval:
                this_interval = intervals[i]

            elif this_interval.end >= intervals[i].start:
                this_interval.end = intervals[i].end

            else:
                new_intervals.append(this_interval)
                this_interval = intervals[i]

            # if this is last
            if i == len(intervals) - 1:
                new_intervals.append(this_interval)

        return new_intervals

# Input:        [[1,4],[2,3]]
# Output:       [[1,3]]
# Expected:     [[1,4]]

intervals = [Interval(1,3),Interval(2,6),Interval(15,18),Interval(8,10)]

s = Solution()
intervals = s.merge(intervals)
print intervals[2].end


