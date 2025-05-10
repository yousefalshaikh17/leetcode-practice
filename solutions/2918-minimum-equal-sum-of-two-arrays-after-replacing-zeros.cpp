// 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
// Topics: Array, Greedy
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/


class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        // Time: O(N + M) (Where N and M are nums1 & nums2 respectively)
        // Space: O(1)

        // Get sums but sub 0s with 1s.
        int sum1 = 0;
        int zeroCount1 = 0;
        for(const int& num : nums1) {
            sum1 += max(num, 1);
            if (num == 0)
                zeroCount1++;
        }

        int sum2 = 0;
        int zeroCount2 = 0;
        for(const int& num : nums2) {
            sum2 += max(num, 1);
            if (num == 0)
                zeroCount2++;
        }

        // Guard clause to prevent proessing on impossible combinations
        if (!zeroCount1 && sum2 > sum1 || !zeroCount2 && sum1 > sum2)
            return -1;
        
        return max(sum1, sum2);
    }
};