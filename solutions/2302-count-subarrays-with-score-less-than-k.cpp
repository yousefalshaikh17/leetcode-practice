// 2302. Count Subarrays With Score Less Than K
// Topics: Array, Binary Search, Sliding Window, Prefix Sum
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/


class Solution {
    public:
        long long countSubarrays(vector<int>& nums, long long k) {
            // Time: O(n)
            // Space: O(1)
            long long numSubarrays = 0;
            long long windowSum = 0;
            int leftIndex = 0;
    
            // Variable Sliding Window
            for (int rightIndex = 0; rightIndex < nums.size(); ++rightIndex) {
                windowSum += nums[rightIndex];
    
                while (leftIndex <= rightIndex && windowSum * (rightIndex - leftIndex + 1) >= k)
                    windowSum -= nums[leftIndex++];
    
                numSubarrays += rightIndex - leftIndex + 1;
            }
    
            return numSubarrays;
        }
    };