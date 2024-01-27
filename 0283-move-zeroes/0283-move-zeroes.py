class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
        
        for j in range(zero_count):
            nums.remove(0)
            
        
        for j in range(zero_count):
            nums.append(0)
            
        return nums