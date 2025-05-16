// 2901. Longest Unequal Adjacent Groups Subsequence II
// Topics: Array, String, Dynamic Programming
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/


class Solution {
public:
    vector<string> getWordsInLongestSubsequence(vector<string>& words,
                                                vector<int>& groups) {
        // Time: O(N^2 * M) Where M is the length of each string in words
        // Space: O(N)

        int wordCount = words.size();
        vector<int> dp(wordCount, 1);
        vector<int> previous(wordCount, -1);
        int maxDpIndex = 0;

        for (int i = 1; i < wordCount; i++) {
            for (int j = 0; j < i; j++)
                if (check(words[i], words[j]) == 1 && dp[j] + 1 > dp[i] &&
                    groups[i] != groups[j]) {
                    dp[i] = dp[j] + 1;
                    previous[i] = j;
                }
            
            if (dp[i] > dp[maxDpIndex])
                maxDpIndex = i;
        }

        vector<string> longestSubsequence;
        // Start at the max
        for (int i = maxDpIndex; i >= 0; i = previous[i])
            longestSubsequence.emplace_back(words[i]);
        
        reverse(longestSubsequence.begin(), longestSubsequence.end());
        return longestSubsequence;
    }

    bool check(string& string1, string& string2) {
        // If the strings are a different size then instantly fail
        if (string1.size() != string2.size())
            return false;
        
        int hammingDistance = 0;
        for (int i = 0; i < string1.size(); i++) {
            hammingDistance += string1[i] != string2[i];
            if (hammingDistance > 1)
                return false;
        }

        // We only return true if the hamming distance is 1
        return hammingDistance == 1;
    }
};