// 1295. Find Numbers with Even Number of Digits
// Topics: Array, Math
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


class Solution {
public:

    bool hasEvenDigits(int num) {
        // Time: O(log M)
        // Space: O(1)
        int num_digits = 0;
        while (num) {
            num_digits++;
            num /= 10;
        }
        return (num_digits & 1) == 0;
    }

    int findNumbers(vector<int>& nums) {
        // Time: O(N log M)
        // Space: O(1)
        int num_even = 0;
        
        for (int num : nums)
            if (hasEvenDigits(num))
                num_even++;

        return num_even;
    }
};

// Alternate slower solution
class Solution {
public:

    bool hasEvenDigits(int num) {
        // Time: O(M)
        // Space: O(1)
        return to_string(num).length() % 2 == 0;
    }

    int findNumbers(vector<int>& nums) {
        // Time: O(N * M)
        // Space: O(1)
        int num_even = 0;
        
        for (int num : nums)
            if (hasEvenDigits(num))
                num_even++;

        return num_even;
    }
};