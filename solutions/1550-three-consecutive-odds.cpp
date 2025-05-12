// 1550. Three Consecutive Odds
// Topics: Array
// https://leetcode.com/problems/three-consecutive-odds/


class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        // Time: O(N)
        // Space: O(1)

        int oddCount = 0;
        for (int i = 0; i < arr.size(); i++)
            if (arr[i] & 1) {
                oddCount++;
                if (oddCount == 3)
                    return true;
            }
            else
                oddCount = 0;

        return false;
    }
};