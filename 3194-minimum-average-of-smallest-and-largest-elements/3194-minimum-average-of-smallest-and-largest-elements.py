class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        
        averages = []
        
        while nums:
            averages.append((nums[0] + nums[-1])/2)
            nums.pop()
            nums.pop(0)
            
            
        return min(averages)