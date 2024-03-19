class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        count = 0
        for i in range(len(nums)):
            if nums[i] < target:
                count += 1
                
        return count