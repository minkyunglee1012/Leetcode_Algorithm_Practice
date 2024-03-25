class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_nums = []
        nums_sum = 0
        
        for i in range(len(nums)):
            nums_sum += nums[i]
            new_nums.append(nums_sum)
            
        return new_nums