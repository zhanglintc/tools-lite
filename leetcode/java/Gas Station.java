// Gas Station
// for leetcode problems
// 2015.03.20 by zhanglin

// Problem:
// There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

// You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
// You begin the journey with an empty tank at one of the gas stations.

// Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

// Note:
// The solution is guaranteed to be unique.

// See Gas Station.py
public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total_remain = 0;
        int car_remain = 0;
        int start = 0;

        for(int i = 0; i < gas.length; i++) {
            total_remain += (gas[i] - cost[i]);

            if(car_remain < 0) {
                car_remain = gas[i] - cost[i];
                start = i;
            }

            else {
                car_remain += gas[i] - cost[i];
            }
        }

        return total_remain >= 0 ? start : -1;
    }
}

