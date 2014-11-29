# Gas Station
# for leetcode problems
# 2014.11.29 by zhanglin

# Problem:
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique.

# Refer to: http://www.cnblogs.com/felixfang/p/3814463.html
# Similar to Maximum Subarray.py
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        total_remain = 0
        car_remain  = 0
        start = 0

        for i in range(len(gas)):
            total_remain += (gas[i] - cost[i]) # always calculate total remain

            if car_remain < 0: # if car's remain less than 0, restart from this station
                car_remain = gas[i] - cost[i]
                start = i

            else: # else only calculate car's remain
                car_remain += (gas[i] - cost[i])

        return start if total_remain >= 0 else -1 # total_remain no less than 0, means must can go circuit


