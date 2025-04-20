# 238. Product of Array Except Self
# Topics: Array, Prefix Sum
# https://leetcode.com/problems/product-of-array-except-self/


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        full_product = 1
        full_product_non_zero = 1
        for num in nums:
            if num != 0:
                full_product_non_zero = full_product_non_zero * num
            else:
                if full_product == 0:
                    full_product_non_zero = 0
            full_product *= num

        for num in nums:
            if num == 0:
                products.append(full_product_non_zero)
            else:
                products.append(int(full_product / num))

        return products