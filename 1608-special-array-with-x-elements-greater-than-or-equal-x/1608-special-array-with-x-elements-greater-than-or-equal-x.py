class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        if len(nums) <= nums[0]:
            return len(nums)
        
        for i in range(1, len(nums)):
            cnt = len(nums) - i
            if nums[i] >= (cnt) and (cnt) > nums[i-1]:
                return cnt
            
        return -1
        
    