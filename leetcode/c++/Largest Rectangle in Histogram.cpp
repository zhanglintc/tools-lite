// Largest Rectangle in Histogram
// for leetcode problems
// 2014.12.24 by zhanglin

// Problem:
// Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
// find the area of largest rectangle in the histogram.

// 7|        _
// 6|      _| |
// 5|     |   |
// 4|     |   |  _
// 3|  _  |   |_| |
// 2| | |_|       |
// 1| |           |
// 0|-----------------
//   0 2 1 5 6 2 3

// Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

// 7|        _
// 6|      _| |
// 5|     |///|
// 4|     |///|  _
// 3|  _  |///|_| |
// 2| | |_|///    |
// 1| |    ///    |
// 0|-----------------
//   0 2 1 5 6 2 3

// The largest rectangle is shown in the shaded area, which has area = 10 unit.

// For example,
// Given height = [2,1,5,6,2,3],
// return 10.

// See Largest Rectangle in Histogram.py
class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        vector<int> stk; // store every start of ascending chain
        int area = 0;    // result
        int this_one = 0;
        int width = 0;

        int i = 0;
        height.push_back(0); // append a 0 makes the code more elegant
        while(i < height.size()) {
            // ascending chain
            if(stk.empty() || height[i] >= height[stk[stk.size() - 1]]) {
                stk.push_back(i);
                i += 1;
            }

            //descending chain
            else {
                this_one = stk.back(); // get last element
                stk.pop_back(); // remove last element
                width = stk.empty() ? i : i - stk[stk.size() - 1] - 1;
                area = area > width * height[this_one] ? area : width * height[this_one];
            }
        }

        return area;
    }
};


