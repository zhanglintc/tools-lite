// Word Break
// for leetcode problems
// 2015.02.04 by zhanglin

// Problem:
// Given a string s and a dictionary of words dict,
// determine if s can be segmented into a space-separated sequence of one or more dictionary words.

// For example, given
// s = "leetcode",
// dict = ["leet", "code"].

// Return true because "leetcode" can be segmented as "leet code".
public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        
        for(int i = 1; i < s.length() + 1; i++) {
            for(int j = 0; j < i; j++) {
                if(dp[j] && dict.contains(s.substring(j, i))) {
                    dp[i] = true;
                }
            }
        }

        return dp[s.length()];
    }
}


