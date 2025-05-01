# 2071. Maximum Number of Tasks You Can Assign
# Topics: Array, Binary Search, Greedy, Queue, Sorting, Monotonic Queue
# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/


from typing import List
from sortedcontainers import SortedList 

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def check_conditions(mid: int) -> bool:
            temp_pills = pills
            worker_strengths = SortedList(workers[len(workers) - mid :])
            for i in range(mid - 1, -1, -1):
                if worker_strengths[-1] >= tasks[i]:
                    worker_strengths.pop()
                else:
                    if temp_pills == 0:
                        return False
                    rep = worker_strengths.bisect_left(tasks[i] - strength)
                    if rep == len(worker_strengths):
                        return False
                    temp_pills -= 1
                    worker_strengths.pop(rep)
            return True


        left,right = 1, min(len(workers), len(tasks))
        max_tasks_completed = 0
        tasks.sort()
        workers.sort()

        while left <= right:
            mid = (left + right) // 2
            if check_conditions(mid):
                max_tasks_completed = mid
                left = mid + 1 
            else:
                right = mid - 1

        return max_tasks_completed