// 75. Sort Colors
// Topics: Array, Two Pointers, Sorting
// https://leetcode.com/problems/sort-colors/

// Two pass solution
class Solution {
public:
    void sortColors(vector<int>& nums) {
        // Time: O(N)
        // Space: O(1)
        int colorCount[3] = {0};
        for (int num: nums)
            colorCount[num]++;


        int currentIndex = 0;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < colorCount[i]; j++) {
                nums[currentIndex] = i;
                currentIndex++;
            }
    }
};

// One pass solution
class Solution {
public:
    void sortColors(vector<int>& nums) {
        // Time: O(N)
        // Space: O(1)
        int left = 0;
        int mid = 0;
        int right = nums.size() - 1;

        while (mid <= right) {
            if (nums[mid] == 0)
                swap(nums[mid++], nums[left++]);
            else if (nums[mid] == 2)
                swap(nums[mid], nums[right--]);
            else
                mid++;
            
        }
    }
};