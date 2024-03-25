class Solution:
    def check(self, nums: List[int]) -> bool:
        sort_nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i:] + nums[:i] == sort_nums:
                return True
            
        return False