class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        
        # Iterate through the list
        for num in nums:
            if num != 0:
                # If the current number is non-zero, place it at the position pointed by non_zero_index
                nums[non_zero_index] = num
                non_zero_index += 1
        
        # Fill the remaining positions with zeros
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
                    
        return nums