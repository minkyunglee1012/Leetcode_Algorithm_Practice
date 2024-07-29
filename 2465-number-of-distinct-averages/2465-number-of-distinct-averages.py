class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        averages = []
        while nums:
            averages.append((nums[0]+nums[-1])/2)
            nums.pop()
            nums.pop(0)
            
        return len(set(averages))