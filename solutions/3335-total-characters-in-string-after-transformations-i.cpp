// 3335. Total Characters in String After Transformations I
// Topics: Hash Table, Math, String, Dynamic Programming, Counting
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/


class Solution {
private:
    static constexpr int mod = 1000000007;
public:
    int lengthAfterTransformations(string s, int t) {
        // Time: O(N + t)
        // Space: O(1)
        int characterCount[26] = {0};
        for (char c: s)
            characterCount[c - 'a']++;

        while (t--) {
            // Modify the array in place instead of making a copy.
            int lastCharacterCount = characterCount[25];
            for (int i = 24; i >= 0; i--)
                characterCount[i + 1] = characterCount[i];
            
            characterCount[0] = lastCharacterCount % mod;
            characterCount[1] = (characterCount[1] + lastCharacterCount) % mod;
        }

        int total = 0;
        for (int count: characterCount)
            total = (total + count) % mod;

        return total;
    }
};