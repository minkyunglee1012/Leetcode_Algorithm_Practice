class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        nums = sorted(nums)
        
        negative_cnt = 0 
        positive_index = len(nums)  

        for i in range(len(nums)):
            if nums[i] < 0:
                negative_cnt += 1
            elif nums[i] > 0 and positive_index == len(nums):
                positive_index = i


        positive_cnt = len(nums) - positive_index
        
        return max(negative_cnt, positive_cnt)
