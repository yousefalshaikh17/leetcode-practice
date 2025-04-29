// 2962. Count Subarrays Where Max Element Appears at Least K Times
// Topics: Array, Sliding Window
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/


class Solution {
    public:
        long long countSubarrays(vector<int>& nums, int k) {
            // Time: O(n)
            // Space: O(1)
            long long numSubarrays = 0;
    
            int maxElement = *max_element(nums.begin(), nums.end());
            int numWindowMaxElements = 0;
    
            // Variable sliding window
            int left = 0;
            for (int right = 0; right < nums.size(); ++right) {
                if (nums[right] == maxElement)
                    ++numWindowMaxElements;
    
                while (numWindowMaxElements == k) {
                    if (nums[left] == maxElement)
                        --numWindowMaxElements;
                    ++left;
                }
    
                numSubarrays += left;
            }
    
            return numSubarrays;
        }
    };