// Largest Rectangle in Histogram
// for leetcode problems
// 2014.12.23 by zhanglin

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

class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        if(height.empty()) {
            return 0;
        }

        int width;
        vector<int> area;
        area.push_back(height[0]);

        for(int i = 0; i < height.size(); i++) {
            width = 1;
            for(int j = i + 1; j < height.size(); j++) {
                if(height[i] <= height[j]) {
                    width += 1;
                }

                else if(height[i] > height[j] || j == height.size() - 1) {
                    area.push_back(height[i] * width);
                }
            }
        }

        return *max_element(area.begin(),area.end());
    }
};


