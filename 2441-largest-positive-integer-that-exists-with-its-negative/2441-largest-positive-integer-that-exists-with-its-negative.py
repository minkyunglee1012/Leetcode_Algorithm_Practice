class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        
        for i in range(len(nums)):
            if nums[i] * (-1) in nums:
                return nums[i]
            
        return -1