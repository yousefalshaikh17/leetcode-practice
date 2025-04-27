// 3392. Count Subarrays of Length Three With a Condition
// Topics: Array
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/


function countSubarrays(nums: number[]): number {
    // Time: O(n)
    // Space: O(1)
    let numSubArrays = 0;

    // No point in starting from index 0.
    // Instead we start at index 2 and look at the 2 previous values.
    for (let i = 2; i < nums.length; i++)
        // Evaluate sum of first and third numbers
        if ((nums[i-2] + nums[i]) * 2 === nums[i-1])
            numSubArrays++;

    return numSubArrays;
};