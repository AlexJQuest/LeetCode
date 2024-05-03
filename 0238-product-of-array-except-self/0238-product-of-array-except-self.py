import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize left and right arrays to store prefix and suffix products respectively
        left_products = [1] * n
        right_products = [1] * n

        # Compute prefix products
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # Compute suffix products
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Multiply prefix and suffix products to get the final result
        result = [left_products[i] * right_products[i] for i in range(n)]

        return result