// 2094. Finding 3-Digit Even Numbers
// Topics: Array, Hash Table, Sorting, Enumeration
// https://leetcode.com/problems/finding-3-digit-even-numbers/


class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        // Time: O(N) (Only the counter initialization)
        // Space: O(1)
        vector<int> uniqueIntegers;

        int digitFrequency[10] = {0};
        for (int i : digits)
            digitFrequency[i]++;

        int currentFrequency[10] = {0};
        for (int i = 100; i < 1000; i++) {
            
            if (i & 1)
                continue;

            int currentDigits[3] = {i / 100, (i / 10) % 10, (i % 10)};
            // Count digits
            for (int i : currentDigits)
                currentFrequency[i]++;

            bool flag = all_of(
                begin(currentDigits),
                end(currentDigits),
                [&digitFrequency, &currentFrequency](int digit) {
                    return digitFrequency[digit] >= currentFrequency[digit];
                });

            if (flag)
                uniqueIntegers.push_back(i);

            // Reset counter
            for (int i : currentDigits)
                currentFrequency[i] = 0;
        }
        
        return uniqueIntegers;
    }
};