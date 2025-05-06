// 1920. Build Array from Permutation
// Topics: Array, Simulation
// https://leetcode.com/problems/build-array-from-permutation/


class Solution {
    public:
        vector<int> buildArray(vector<int>& nums) {
            // Time: O(N)
            // Space: O(1)
            vector<int> ans(nums.size());
    
            for (int i = 0; i < nums.size(); i++)
                ans[i] = nums[nums[i]];
    
            return ans;
        }
    };