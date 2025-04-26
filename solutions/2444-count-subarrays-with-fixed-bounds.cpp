// 2444. Count Subarrays With Fixed Bounds
// Topics: Array, Queue, Sliding Window, Monotonic Queue
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/


class Solution {
    public:
        long long countSubarrays(vector<int>& nums, int minK, int maxK) {
            // Time: O(n)
            // Space: O(1)
            long long numSubarrays = 0;
            int minPos = -1, maxPos = -1, badPos = -1;
    
            for (int i = 0; i < nums.size(); ++i) {
                int num = nums[i];
                if (num < minK || num > maxK)
                    badPos = i;
                if (num == minK)
                    minPos = i;
                if (num == maxK)
                    maxPos = i;
    
                numSubarrays += max(0, min(minPos, maxPos) - badPos);
            }
    
            return numSubarrays;
        }
    };
    