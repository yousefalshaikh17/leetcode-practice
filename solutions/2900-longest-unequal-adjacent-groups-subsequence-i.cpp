// 2900. Longest Unequal Adjacent Groups Subsequence I
// Topics: Array, String, Dynamic Programming, Greedy
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/


class Solution {
public:
    vector<string> getLongestSubsequence(vector<string>& words, vector<int>& groups) {
        // Time: O(N)
        // Space: O(1)

        vector<string> sequence;

        int lastBinaryDigit = -1; // Temporary

        for (int i = 0; i < words.size(); i++)
            if (groups[i] != lastBinaryDigit) {
                sequence.push_back(words[i]);
                lastBinaryDigit = groups[i];
            }

        return sequence;
    }
};