// 3337. Total Characters in String After Transformations II
// Topics: Hash Table, Math, String, Dynamic Programming, Counting
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/


class Solution {
private:
    static constexpr int mod = 1000000007;

    array<array<int, 26>, 26> multiplyMatrices(const array<array<int, 26>, 26>& A,
                                               const array<array<int, 26>, 26>& B) {
        array<array<int, 26>, 26> result = {0};

        for (int i = 0; i < 26; i++)
            for (int j = 0; j < 26; j++) {
                __int128 sum = 0;
                for (int k = 0; k < 26; k++)
                    sum += (__int128) A[i][k] * B[k][j];
                result[i][j] = sum % mod;
            }

        return result;
    }

    array<array<int, 26>, 26> powerMatrix(array<array<int, 26>, 26>& matrix, int exp) {
        int n = matrix.size();
        array<array<int, 26>, 26> result = {0};

        for (int i = 0; i < n; i++) result[i][i] = 1;
        while (exp > 0) {
            if (exp & 1) // Check if odd
                result = multiplyMatrices(result, matrix);
            matrix = multiplyMatrices(matrix, matrix);
            exp >>= 1;
        }
        return result;
    }
public:
    int lengthAfterTransformations(string s, int t, vector<int>& nums) {
        // Time: O(N + log t)
        // Space: O(1)

        array<array<int, 26>, 26> transform = {0};
        for (int i = 0; i < 26; i++)
            for (int j = 0; j < nums[i]; j++)
                transform[i][(i + j + 1) % 26]++;

        array<array<int, 26>, 26> characterCountMatrix = {0};
        for (char ch : s) 
            characterCountMatrix[0][ch - 'a']++;

        transform = powerMatrix(transform, t);
        characterCountMatrix = multiplyMatrices(characterCountMatrix, transform);
        
        int total = 0;

        for (int cnt : characterCountMatrix[0]) 
            total = (total + cnt) % mod;
        
        return total;

    }
};