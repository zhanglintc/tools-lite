// Permutations
// for leetcode problems
// 2014.09.27 by zhanglin

// Problem:
// Given a collection of numbers, return all possible permutations.

// For example,
// [1,2,3] have the following permutations:
// [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

// See Permutations.py
class Solution
{
public:
    vector<vector<int>> permute(vector<int> &num)
    {
        // FixNum + sorted_vect
        int FixNum;
        vector<vector<int>> final_vect;
        vector<vector<int>> sorted_vect;

        if(num.size() == 1)
        {
            final_vect.push_back(num);
            return final_vect;
        }

        for(int i = 0; i < num.size(); i++)
        {
            // put each element of 'num' to the end one by one,
            // pop the last element and store it as FixNum,
            // then sort 'num' and concatenate FixNum and these results.

            swap(num[i], num[num.size() - 1]); // put num[i] to the end
            FixNum = num[num.size() - 1]; // store it as FixNum
            num.pop_back(); // shorten the 'num'

            sorted_vect = permute(num); // sort the shorten 'num'
            for(int j = 0; j < sorted_vect.size(); j++) // in these results
            {
                sorted_vect[j].push_back(FixNum); // add FixNum to them
                final_vect.push_back(sorted_vect[j]); // put it to the result vector
            }

            // restore to the original
            num.push_back(FixNum);
            swap(num[i], num[num.size() - 1]);
        }

        return final_vect; // :D
    }
};


