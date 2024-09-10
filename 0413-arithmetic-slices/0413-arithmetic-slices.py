class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        
        # dynamic programming 
        cnt = 0
        current = 0
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current += 1
                cnt += current
                
            else:
                current = 0
                
        return cnt