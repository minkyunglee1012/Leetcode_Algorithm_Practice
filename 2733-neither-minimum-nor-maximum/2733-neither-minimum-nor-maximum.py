class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        
        nums = sorted(nums)
        nums.pop(0)
        nums.pop()
        
        return nums[0]