# 15. 3Sum
# Topics: Array, Two Pointers, Sorting
# https://leetcode.com/problems/3sum/


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        triplets = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L,R = i+1, len(nums)-1
            while L < R:
                result = nums[i] + nums[L] + nums[R]
                if result == 0:
                    triplets.append([nums[i], nums[L], nums[R]])
                    R -= 1
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1
                    continue

                if result > 0:
                    R -= 1
                else:
                    L += 1
                
        return triplets