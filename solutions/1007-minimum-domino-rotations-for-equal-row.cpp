// 1007. Minimum Domino Rotations For Equal Row
// Topics: Array, Greedy
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/


class Solution {
    public:
        int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
            // Time: O(N)
            // Space: O(1)
            
            int minimumRotations = tops.size() + 1;
    
            // Check for each possible domino value
            for (int i = 1; i <= 6; i++) {
                int topCount = 0;
                int bottomCount = 0;
                bool valid = true;
    
                for (int j = 0; j < tops.size(); j++) {
                    if (tops[j] == i && bottoms[j] == i)
                        continue;
    
                    if (tops[j] == i)
                        topCount ++;
                    else if (bottoms[j] == i)
                        bottomCount += 1;
                    else {
                        valid = false;
                        break;
                    }
                }
    
                if (!valid)
                    continue;
    
                minimumRotations = std::min({minimumRotations, topCount, bottomCount});
                if (minimumRotations == 0)
                    break;
            }
            return (minimumRotations <= tops.size()) ? minimumRotations : -1;
        }
    };