// 3341. Find Minimum Time to Reach Last Room I
// Topics: Array, Graph, Heap (Priority Queue), Matrix, Shortest Path
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/


class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        // Time: O(N * M * log(N * M))
        // Space: O(N * M)

        int n = moveTime.size();        // Rows
        int m = moveTime[0].size();     // Columns

        vector<vector<int>> distances(n, vector<int>(m, INT_MAX));
        distances[0][0] = moveTime[0][0];

        std::array<pair<int, int>, 4> directions = {{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> priorityQueue;
        priorityQueue.push({0, 0, 0}); // {currentTime, row, col}

        while (!priorityQueue.empty()) {
            // Get the point with the lowest cost (Initially source)
            int time = priorityQueue.top()[0];
            int row = priorityQueue.top()[1];
            int col = priorityQueue.top()[2];
            priorityQueue.pop();

            // Ignore if a lower cost was already found
            if (time > distances[row][col])
                continue;

            // If this is the target point, return time.
            if (row == n - 1 && col == m - 1)
                return time;

            // Add neighbors to queue
            for (pair<int, int>& dir : directions) {
                int newRow = row + dir.first;
                int newCol = col + dir.second;

                if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= m)
                    continue;

                int arrivalTime = max(time, moveTime[newRow][newCol]) + 1;

                if (arrivalTime < distances[newRow][newCol]) {
                    distances[newRow][newCol] = arrivalTime;
                    priorityQueue.push({arrivalTime, newRow, newCol});
                }
            }
        }

        // Return targets distance
        return -1;
    }
};